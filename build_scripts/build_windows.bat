@echo off
REM Build script for Windows executable using PyInstaller

echo Building CSV Splitter GUI for Windows...

REM Check if PyInstaller is installed
python -c "import PyInstaller" 2>nul
if errorlevel 1 (
    echo PyInstaller not found. Installing...
    pip install pyinstaller
)

REM Clean previous builds
if exist "dist" rmdir /s /q dist
if exist "build" rmdir /s /q build

REM Create the executable
echo Creating Windows executable...
pyinstaller --clean ^
    --onefile ^
    --windowed ^
    --name "CSV-Splitter-GUI" ^
    --add-data "src/csv_splitter;csv_splitter" ^
    --hidden-import "csv_splitter" ^
    --hidden-import "csv_splitter.gui" ^
    --hidden-import "csv_splitter.processor" ^
    --hidden-import "csv_splitter.config" ^
    --hidden-import "csv_splitter.exceptions" ^
    --hidden-import "csv_splitter.ui_components" ^
    --hidden-import "csv_splitter.logger" ^
    main.py

if exist "dist\CSV-Splitter-GUI.exe" (
    echo.
    echo ✓ Build successful!
    echo Executable created: dist\CSV-Splitter-GUI.exe
    echo File size: 
    dir "dist\CSV-Splitter-GUI.exe" | findstr "CSV-Splitter-GUI.exe"
) else (
    echo.
    echo ✗ Build failed!
    exit /b 1
)

echo.
echo To distribute:
echo 1. Test the executable: dist\CSV-Splitter-GUI.exe
echo 2. The executable is self-contained and includes all dependencies
echo 3. Users can run it on Windows without installing Python

pause