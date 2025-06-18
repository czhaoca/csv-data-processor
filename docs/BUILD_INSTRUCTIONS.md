# Build Instructions

This document provides instructions for building standalone executables of CSV Splitter GUI for distribution.

## Overview

The CSV Splitter GUI can be built into standalone executables for Windows, macOS, and Linux using PyInstaller. This allows users to run the application without installing Python or any dependencies.

## Prerequisites

### All Platforms
- Python 3.7 or higher
- PyInstaller (automatically installed by build scripts)

### Platform-Specific Requirements

#### Windows
- Windows 10 or later (for building)
- No additional requirements

#### macOS
- macOS 10.10 or later (for building)
- Xcode Command Line Tools (for some dependencies)

#### Linux
- Any modern Linux distribution
- Development packages for tkinter (usually pre-installed)

## Quick Build

### Automatic Cross-Platform Build

The easiest way to build for your current platform:

```bash
python build_scripts/build_cross_platform.py
```

This script will:
1. Detect your platform automatically
2. Install PyInstaller if needed
3. Run the appropriate build process
4. Create a standalone executable in the `dist/` directory

## Platform-Specific Builds

### Windows Executable (.exe)

#### Using Build Script
```cmd
build_scripts\build_windows.bat
```

#### Manual Build
```cmd
pip install pyinstaller
pyinstaller --clean --onefile --windowed --name "CSV-Splitter-GUI" --add-data "src/csv_splitter;csv_splitter" main.py
```

**Output**: `dist/CSV-Splitter-GUI.exe`

**Features**:
- Single executable file
- No console window
- Self-contained (includes all dependencies)
- Compatible with Windows 10+

### macOS Application (.app)

#### Using Build Script
```bash
bash build_scripts/build_macos.sh
```

#### Manual Build
```bash
pip install pyinstaller
pyinstaller --clean --onefile --windowed --name "CSV-Splitter-GUI" --add-data "src/csv_splitter:csv_splitter" main.py
```

**Output**: `dist/CSV Splitter GUI.app`

**Features**:
- macOS application bundle
- Drag-and-drop installation
- Native macOS integration
- Self-contained
- Compatible with macOS 10.10+

### Linux Executable

#### Using Cross-Platform Script
```bash
python build_scripts/build_cross_platform.py
```

#### Manual Build
```bash
pip install pyinstaller
pyinstaller --clean --onefile --windowed --name "CSV-Splitter-GUI" --add-data "src/csv_splitter:csv_splitter" main.py
```

**Output**: `dist/CSV-Splitter-GUI`

**Features**:
- Single executable file
- Self-contained
- Compatible with most Linux distributions

## Build Configuration

### PyInstaller Options Explained

- `--clean`: Remove build cache before building
- `--onefile`: Create a single executable file
- `--windowed`: No console window (GUI only)
- `--name`: Name of the executable
- `--add-data`: Include source code in the bundle
- `--hidden-import`: Explicitly import modules that might be missed

### Customizing Builds

#### Adding an Icon

1. Create an icon file:
   - Windows: `.ico` format
   - macOS: `.icns` format  
   - Linux: `.png` format

2. Add to build command:
   ```bash
   pyinstaller --icon=path/to/icon.ico ...
   ```

#### Optimizing Size

To reduce executable size:

1. Use `--exclude-module` to remove unused modules:
   ```bash
   pyinstaller --exclude-module matplotlib --exclude-module numpy ...
   ```

2. Use UPX compression (if available):
   ```bash
   pyinstaller --upx-dir=/path/to/upx ...
   ```

## Troubleshooting

### Common Issues

#### "Module not found" errors
- Solution: Add missing modules with `--hidden-import`
- Example: `--hidden-import csv_splitter.processor`

#### Large executable size
- Normal for PyInstaller builds (typically 20-50MB)
- Includes Python interpreter and all dependencies
- Consider using `--exclude-module` for unused packages

#### macOS "App is damaged" warning
- Solution: Code signing (requires Apple Developer account)
- Alternative: Users can right-click → Open to bypass

#### Windows antivirus false positives
- Common with PyInstaller executables
- Solution: Code signing or whitelisting

### Testing Builds

#### Windows
```cmd
dist\CSV-Splitter-GUI.exe
```

#### macOS
```bash
open "dist/CSV Splitter GUI.app"
```

#### Linux
```bash
./dist/CSV-Splitter-GUI
```

## Distribution

### Creating Release Packages

#### Windows
- Distribute the `.exe` file directly
- Optionally create an installer with NSIS or similar

#### macOS
- Create a DMG file:
  ```bash
  hdiutil create -volname "CSV Splitter GUI" -srcfolder "dist/CSV Splitter GUI.app" -ov -format UDZO "CSV-Splitter-GUI-macOS.dmg"
  ```

#### Linux
- Distribute the executable directly
- Consider creating a `.deb` or `.rpm` package
- Or create a tarball:
  ```bash
  tar -czf CSV-Splitter-GUI-linux.tar.gz -C dist CSV-Splitter-GUI
  ```

### File Sizes (Approximate)

- Windows: 25-35 MB
- macOS: 30-40 MB  
- Linux: 25-35 MB

These sizes include the Python interpreter and all dependencies, making the executables completely self-contained.

## CI/CD Integration

### GitHub Actions Example

```yaml
name: Build Releases

on:
  release:
    types: [published]

jobs:
  build:
    strategy:
      matrix:
        os: [windows-latest, macos-latest, ubuntu-latest]
    
    runs-on: ${{ matrix.os }}
    
    steps:
    - uses: actions/checkout@v3
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: pip install pyinstaller
    
    - name: Build executable
      run: python build_scripts/build_cross_platform.py
    
    - name: Upload artifacts
      uses: actions/upload-artifact@v3
      with:
        name: executable-${{ matrix.os }}
        path: dist/
```

## Development Builds

For development and testing:

```bash
# Install in development mode
pip install -e .

# Run directly
python main.py

# Or use installed command
csv-splitter-gui
```

This approach is faster for development but requires Python to be installed.

## Support

If you encounter issues building executables:

1. Check that all dependencies are installed
2. Verify the build scripts have execute permissions (macOS/Linux)
3. Try the manual build commands
4. Check the PyInstaller documentation for platform-specific issues

For additional help, please refer to the project documentation or create an issue in the project repository.