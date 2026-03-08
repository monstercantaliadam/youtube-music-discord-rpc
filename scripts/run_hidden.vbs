Set shell = CreateObject("WScript.Shell")
Dim projectRoot
projectRoot = CreateObject("Scripting.FileSystemObject").GetParentFolderName(CreateObject("Scripting.FileSystemObject").GetParentFolderName(WScript.ScriptFullName))
shell.Run "pythonw.exe """ & projectRoot & "\src\youtube_music_rpc\main.py""", 0, False
