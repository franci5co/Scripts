Set objLocator = CreateObject("WbemScripting.SWbemLocator")
Set objService = objLocator.ConnectServer(".", "root\cimv2")
Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objFile = objFSO.CreateTextFile("C:\ScriptLog.txt", False)
Set objFile = objFSO.OpenTextFile("C:\FSO\ScriptLog.txt", 2)

objService.Security_.ImpersonationLevel = 3
Set Disks = _
    objService.ExecQuery("select name,freespace from win32_volume where drivetype=3 AND driveletter=NULL")
i=0
For each Disk in Disks
    i = i+1   
    objFile.WriteLine Disk.name & "  " _
        & Disk.freespace & VBNewLine
Next
If i = 0 Then
    objFile.WriteLine "No Jobs Scheduled with the AT command were found"
End If
objFile.Close