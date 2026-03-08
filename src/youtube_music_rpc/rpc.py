from __future__ import annotations

import asyncio
import json
import logging
import time
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Optional

from pypresence import AioPresence
from winsdk.windows.media.control import (
    GlobalSystemMediaTransportControlsSessionManager as SessionManager,
)

logger = logging.getLogger(__name__)


@dataclass
class MediaInfo:
    title: str
    artist: str
    album: str
    is_playing: bool
    position: float
    end_time: float


class CoverArtResolver:
    def __init__(self) -> None:
        self._current_song_id: Optional[str] = None
        self._current_cover_url = "youtube_music"

    def resolve(self, title: str, artist: str) -> str:
        song_id = f"{title}-{artist}"
        if song_id == self._current_song_id:
            return self._current_cover_url

        self._current_song_id = song_id
        self._current_cover_url = self._fetch_cover(title, artist)
        return self._current_cover_url

    @staticmethod
    def _fetch_cover(title: str, artist: str) -> str:
        try:
            query = urllib.parse.quote(f"{title} {artist}")
            url = f"https://itunes.apple.com/search?term={query}&entity=song&limit=1"
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(request, timeout=3) as response:
                payload = json.loads(response.read().decode())
                if payload.get("resultCount", 0) > 0:
                    artwork_url = payload["results"][0].get("artworkUrl100")
                    if artwork_url:
                        return artwork_url.replace("100x100bb", "512x512bb")
        except Exception as exc:  # pragma: no cover - network variability
            logger.warning("Could not fetch cover art: %s", exc)
        return "youtube_music"


class YouTubeMusicRPC:
    def __init__(self, client_id: str, supported_apps: list[str], poll_interval: int, button_label: str, buttons_enabled: bool) -> None:
        self.client_id = client_id
        self.supported_apps = supported_apps
        self.poll_interval = max(15, poll_interval)
        self.button_label = button_label
        self.buttons_enabled = buttons_enabled
        self.rpc = AioPresence(client_id)
        self.connected = False
        self.cover_resolver = CoverArtResolver()

    async def connect(self) -> None:
        if self.connected:
            return
        await self.rpc.connect()
        self.connected = True
        logger.info("Connected to Discord Rich Presence.")

    async def disconnect(self) -> None:
        try:
            await self.rpc.clear()
        except Exception:
            pass
        self.connected = False

    async def get_media_info(self) -> Optional[MediaInfo]:
        sessions = await SessionManager.request_async()
        current_session = sessions.get_current_session()
        if not current_session:
            return None

        app_id = (current_session.source_app_user_model_id or "").lower()
        logger.debug("Detected media source: %s", app_id)
        if not any(app in app_id for app in self.supported_apps):
            return None

        info = await current_session.try_get_media_properties_async()
        timeline = current_session.get_timeline_properties()
        playback_info = current_session.get_playback_info()
        is_playing = playback_info.playback_status == 4

        return MediaInfo(
            title=info.title or "Unknown title",
            artist=info.artist or "Unknown artist",
            album=info.album_title or "",
            is_playing=is_playing,
            position=timeline.position.total_seconds() if timeline else 0,
            end_time=timeline.end_time.total_seconds() if timeline else 0,
        )

    async def update_presence(self, media: MediaInfo) -> None:
        cover_url = self.cover_resolver.resolve(media.title, media.artist)
        details = media.title[:128]
        state = f"by {media.artist}"
        if media.album.strip():
            state += f" • {media.album}"
        state = state[:128]

        start_time = int(time.time() - media.position) if media.position >= 0 else None
        end_time = None
        if media.end_time > 0:
            remaining_time = max(0, media.end_time - media.position)
            end_time = int(time.time() + remaining_time)

        payload = {
            "details": details,
            "state": state,
            "large_image": cover_url,
            "large_text": media.title[:128],
            "small_image": "youtube_music",
            "small_text": "YouTube Music",
            "start": start_time,
            "end": end_time,
        }

        if self.buttons_enabled:
            search_query = urllib.parse.quote(f"{media.title} {media.artist}")
            payload["buttons"] = [{
                "label": self.button_label[:32],
                "url": f"https://music.youtube.com/search?q={search_query}",
            }]

        try:
            await self.rpc.update(**payload)
            logger.info("Presence updated: %s - %s", media.title, media.artist)
        except Exception as exc:
            logger.warning("Detailed presence update failed, retrying with fallback assets: %s", exc)
            fallback_payload = {
                "details": details,
                "state": state,
                "large_image": "youtube_music",
                "large_text": "YouTube Music",
                "start": start_time,
                "end": end_time,
            }
            await self.rpc.update(**fallback_payload)

    async def run(self) -> None:
        logger.info("Starting YouTube Music Discord RPC service.")
        while True:
            try:
                if not self.connected:
                    try:
                        await self.connect()
                    except Exception as exc:
                        logger.error("Failed to connect to Discord: %s", exc)
                        await asyncio.sleep(self.poll_interval)
                        continue

                media = await self.get_media_info()
                if media and media.is_playing:
                    await self.update_presence(media)
                else:
                    try:
                        await self.rpc.clear()
                    except Exception as exc:
                        logger.debug("Could not clear presence: %s", exc)

                await asyncio.sleep(self.poll_interval)
            except Exception as exc:
                logger.exception("Unexpected error in main loop: %s", exc)
                self.connected = False
                await asyncio.sleep(self.poll_interval)
