set curDir=%~dp0
set targetDir=%1
set docDir=%2

AnyRepTool AMMR.xml %targetDir% AnyScriptPackage.anyml.xslt %docDir%

pause


