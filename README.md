# CSV Splitter GUI

A modern, modular Python GUI application for splitting CSV files based on user-selected criteria.

## Quick Start

```bash
# Clone the repository
git clone <repository-url>
cd csv-splitter-gui

# Run the application
python main.py
```

## Features

- **Multi-field grouping**: Group data by single or multiple field combinations
- **Flexible field selection**: Choose exactly which fields to include in output files  
- **Intuitive GUI**: Clean, modern interface with real-time feedback
- **Memory efficient**: Handles large files without loading entire dataset
- **Cross-platform**: Works on Windows, macOS, and Linux

## Documentation

- **[Getting Started](GETTING_STARTED.md)**: Quick start guide for users and developers
- **[User Guide](docs/USER_GUIDE.md)**: Comprehensive documentation and usage instructions
- **[Build Instructions](docs/BUILD_INSTRUCTIONS.md)**: How to create standalone executables
- **[Release Info](RELEASES.md)**: Download options and release details
- **[Architecture](docs/ARCHITECTURE.md)**: Technical architecture and design details  
- **[Project Structure](docs/PROJECT_STRUCTURE.md)**: Codebase organization and development guide

## Requirements

- Python 3.7+
- tkinter (included with most Python installations)
- No external runtime dependencies

## Installation

### Download Pre-built Binaries

1. Go to the [Releases](https://github.com/czhaoca/csv-splitter-gui/releases) page
2. Download the latest version for your operating system:
   - **Windows**: `CSV-Splitter-GUI.exe`
   - **macOS**: `CSV-Splitter-GUI-macOS.zip` (extract and run the `.app`)
   - **Linux**: Build from source (see below)

3. Run the downloaded executable

#### Windows Security Warning

If you see "Windows protected your PC" warning:
1. Click "More info"
2. Click "Run anyway"

Or right-click the .exe → Properties → Check "Unblock" → OK

*Note: The executable is not code-signed. See [Code Signing Guide](docs/CODE_SIGNING.md) for details.*

### Run from Source

```bash
python main.py
```

### Install as Package
```bash
pip install -e .
csv-splitter-gui
```

### Generate Test Data
```bash
python examples/generate_test_data.py
```

## Project Structure

```
csv-splitter-gui/
├── src/csv_splitter/        # Main application package
├── tests/                   # Test suite
├── docs/                    # Documentation
├── examples/               # Sample data and generators
├── build_scripts/          # Build and packaging tools
└── main.py                # Application entry point
```

## Development

```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/

# Code formatting
black src/ tests/

# Build standalone executable
python build_scripts/build_cross_platform.py
```

## License

MIT License - see documentation for details.