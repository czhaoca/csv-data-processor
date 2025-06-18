# Release Information

## Available Releases

CSV Splitter GUI is available in multiple formats to suit different user preferences and technical requirements.

### Version 2.0.0

#### 🐍 Python Source (Recommended for Developers)

**Requirements**: Python 3.7+, tkinter

```bash
# Clone repository
git clone <repository-url>
cd csv-splitter-gui

# Run directly
python main.py

# Or install as package
pip install -e .
csv-splitter-gui
```

**Advantages**:
- Smallest download size
- Easy to modify and extend
- Access to latest features
- Full development environment

#### 📦 Standalone Executables (Recommended for End Users)

Self-contained executables that don't require Python installation.

##### Windows (.exe)
- **File**: `CSV-Splitter-GUI.exe`
- **Size**: ~25-35 MB
- **Requirements**: Windows 10 or later
- **Installation**: Download and run directly

##### macOS (.app)
- **File**: `CSV Splitter GUI.app`
- **Size**: ~30-40 MB  
- **Requirements**: macOS 10.10 or later
- **Installation**: Download and drag to Applications folder

##### Linux (executable)
- **File**: `CSV-Splitter-GUI`
- **Size**: ~25-35 MB
- **Requirements**: Most modern Linux distributions
- **Installation**: Download, make executable, and run

## Building Your Own Releases

### Quick Build (Any Platform)

```bash
# Install build dependencies
pip install pyinstaller

# Auto-detect platform and build
python build_scripts/build_cross_platform.py
```

### Platform-Specific Builds

#### Windows
```cmd
build_scripts\build_windows.bat
```

#### macOS
```bash
bash build_scripts/build_macos.sh
```

#### Linux
```bash
python build_scripts/build_cross_platform.py
```

## Release Features

### What's Included in Standalone Executables

✅ **Complete Application**
- Full CSV Splitter GUI functionality
- All dependencies bundled
- No Python installation required

✅ **Self-Contained**
- Single file (Windows/Linux) or app bundle (macOS)
- No additional downloads needed
- Portable - can run from any location

✅ **Native Integration**
- Platform-appropriate file dialogs
- Native look and feel
- Standard application behavior

### What's NOT Included

❌ **Source Code Access**
- Cannot modify application behavior
- No development tools included
- For customization, use Python source version

❌ **Additional Tools**
- No command-line utilities
- No development dependencies
- No test suite

## Download Recommendations

### For End Users
👥 **Choose**: Standalone executable for your platform
- ✅ No technical setup required
- ✅ Double-click to run
- ✅ Standard installation experience

### For Developers
👨‍💻 **Choose**: Python source version
- ✅ Full source code access
- ✅ Can modify and extend
- ✅ Latest features and updates
- ✅ Development tools included

### For System Administrators
🏢 **Choose**: Based on deployment needs
- **Large deployments**: Python source with shared Python installation
- **Isolated deployments**: Standalone executables
- **Mixed environments**: Both options available

## Security Notes

### Code Signing Status

- **Windows**: Unsigned (may trigger SmartScreen warning)
- **macOS**: Unsigned (may require right-click → Open)
- **Linux**: No signing required

### Antivirus Considerations

Some antivirus software may flag PyInstaller-generated executables as potentially unwanted programs (PUPs). This is a false positive common with many Python applications bundled with PyInstaller.

**If flagged**:
1. Verify download from official source
2. Add to antivirus whitelist
3. Consider building from source

### Verification

For security-conscious users:
1. Download source code
2. Build your own executable using provided scripts
3. Compare checksums with provided hashes (when available)

## Support

### Compatibility

| Platform | Minimum Version | Tested Versions |
|----------|----------------|-----------------|
| Windows  | Windows 10     | 10, 11         |
| macOS    | 10.10          | 10.15, 11, 12  |
| Linux    | Most distros   | Ubuntu, Fedora, Debian |

### Getting Help

1. **Documentation**: Check `docs/` folder for detailed guides
2. **Issues**: Report problems via project issue tracker
3. **Source**: Review source code for technical details

### Performance Notes

- **Startup Time**: Standalone executables may take 2-5 seconds to start (normal for PyInstaller)
- **Memory Usage**: ~50-100MB RAM (includes Python interpreter)
- **File Size Limits**: Can handle files limited by available system memory

## Changelog

See `CHANGELOG.md` for detailed version history and feature changes.

---

**Latest Release**: v2.0.0  
**Release Date**: 2025-06-18  
**Build System**: PyInstaller 5.0+