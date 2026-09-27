@echo off


set "specPath=./pyinstaller.spec"
set "envName=EVT"


if exist "build" (
    rd /s /q "build"
)
if exist "dist" (
    rd /s /q "dist"
)


if exist "%specPath%" (
    echo "Activating conda environment: %envName%"
    call conda activate %envName%
    echo "Building app via PyInstaller..."
    pyinstaller "%specPath%"
) else (
    echo "Error: Spec file %specPath% not found!"
    pause
    exit /b 1
)


if %errorlevel% neq 0 (
    echo "Failed:("
    echo %errorlevel%
    pause
    exit /b %errorlevel%
) else (
    echo "Succeeded:)"
    pause
)