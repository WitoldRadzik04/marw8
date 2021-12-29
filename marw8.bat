@echo off
if "%1"=="" goto nothing
if %1==help goto help
if %1==start goto starting
if %1==setup goto setup
if %1==info goto info

echo Command not found. For help, type ^"marw8 help^"

:nothing
echo marw8 requires an argument. To display a list of all commands, type ^"marw8 help^"
goto commonexit

:help
type %~dp0\help.txt 
goto commonexit

:starting
%~dp0\main.py
goto commonexit

:setup 
%~dp0\setup.py
goto commonexit

:info
type %~dp0\readme.md
goto commonexit

:commonexit
