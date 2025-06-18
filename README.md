# CSV Splitter GUI

A modern, cross-platform Python GUI application for splitting CSV files based on user-selected criteria.

## Features

- **Multi-field splitting**: Split data by single or multiple field combinations
- **Flexible field selection**: Choose exactly which fields to include in output files  
- **Intuitive GUI**: Clean, modern interface with real-time feedback
- **Memory efficient**: Handles large files without loading entire dataset
- **Cross-platform**: Works on Windows, macOS, and Linux

## Quick Start

### Download Pre-built Binaries (Recommended)

1. Go to the [Releases](https://github.com/czhaoca/csv-splitter-gui/releases) page
2. Download the latest version for your operating system:
   - **Windows**: `CSV-Splitter-GUI.exe`
   - **macOS**: `CSV-Splitter-GUI-macOS.zip` (extract and run the `.app`)
   - **Linux**: Build from source (see below)

3. Run the downloaded executable

#### Windows Security Warning

If you see "Windows protected your PC" warning:
1. Click "More info" → "Run anyway"
2. Or right-click the .exe → Properties → Check "Unblock" → OK

*The executable is not code-signed. See [Code Signing Guide](docs/CODE_SIGNING.md) for details.*

### Run from Source

```bash
# Clone the repository
git clone https://github.com/czhaoca/csv-splitter-gui.git
cd csv-splitter-gui

# Run the application
python main.py
```

### Install as Package

```bash
pip install -e .
csv-splitter-gui
```

## Documentation

- **[User Guide](docs/USER_GUIDE.md)**: Complete usage instructions and tutorials
- **[Build Instructions](docs/BUILD_INSTRUCTIONS.md)**: Create standalone executables
- **[Code Signing Guide](docs/CODE_SIGNING.md)**: Windows security and distribution
- **[Architecture](docs/ARCHITECTURE.md)**: Technical design and architecture
- **[Project Structure](docs/PROJECT_STRUCTURE.md)**: Codebase organization

## Requirements

- Python 3.7+
- tkinter (included with most Python installations)
- No external runtime dependencies

## Development

```bash
# Install development dependencies
pip install -r requirements.txt

# Generate test data
python examples/generate_test_data.py

# Run tests
python -m pytest tests/

# Code formatting
black src/ tests/

# Build executable
python build_scripts/build_cross_platform.py
```

## Project Structure

```
csv-splitter-gui/
├── src/csv_splitter/        # Main application package
├── tests/                   # Test suite
├── docs/                    # Documentation
├── examples/                # Sample data and generators
├── build_scripts/           # Build tools and PyInstaller specs
├── .github/workflows/       # CI/CD automation
└── main.py                  # Application entry point
```

## License

MIT License - see [LICENSE](LICENSE) for details.