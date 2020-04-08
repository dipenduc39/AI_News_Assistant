Set shell = CreateObject("WScript.Shell")
shell.CurrentDirectory = "your project directory"
shell.Run "python AI_News.py",0
Set WshShell = Nothing 