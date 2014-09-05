Const ForReading = 1
Const ForWriting = 2

Set objFSO = CreateObject("Scripting.FileSystemObject")
Set WshShell = WScript.CreateObject("Wscript.Shell")
vAPPDATA = WshShell.ExpandEnvironmentStrings("%APPDATA%")
if objfso.FileExists(vAPPDATA & "\SAP\Common\saplogon.ini") Then
	Set objFile = objFSO.OpenTextFile(vAPPDATA & "\SAP\Common\saplogon.ini", ForReading)

	strText = objFile.ReadAll
	objFile.Close
	strNewText = Replace(strText, "00 PRD CAP ENTEL ERP PRD", "00 CAP ENTEL PRODUCTIVO")


	Set objFile = objFSO.OpenTextFile(vAPPDATA & "\SAP\Common\saplogon.ini", ForWriting)
	objFile.WriteLine strNewText
	objFile.Close

	Set objFile = objFSO.OpenTextFile(vAPPDATA & "\SAP\Common\saplogon.ini", ForReading)

	strText = objFile.ReadAll
	objFile.Close
	strNewText = Replace(strText, "01 PRD CAP ENTEL ERP PRD SAPROUTER", "01 CAP ENTEL PRODUCTIVO INTERNET")

	Set objFile = objFSO.OpenTextFile(vAPPDATA & "\SAP\Common\saplogon.ini", ForWriting)
	objFile.WriteLine strNewText
	objFile.Close
End If