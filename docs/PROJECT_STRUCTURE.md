# Project Structure

This document describes the organization and structure of the CSV Splitter GUI project.

## Directory Layout

```
csv-splitter-gui/
├── src/                     # Source code package
│   └── csv_splitter/        # Main application package
│       ├── __init__.py      # Package initialization
│       ├── config.py        # Configuration and constants
│       ├── exceptions.py    # Custom exception classes
│       ├── processor.py     # Core CSV processing logic
│       ├── gui.py          # Main GUI application
│       ├── ui_components.py # Reusable UI components
│       └── logger.py       # Logging configuration
├── tests/                   # Test suite
│   ├── __init__.py         # Test package initialization
│   ├── test_modular_app.py # Comprehensive module tests
│   └── test_gui_functionality.py # GUI functionality tests
├── docs/                    # Documentation
│   ├── USER_GUIDE.md       # Main project documentation
│   ├── ARCHITECTURE.md     # Architecture documentation
│   ├── PROJECT_STRUCTURE.md # This file
│   └── BUILD_INSTRUCTIONS.md # Build and release guide
├── examples/               # Example data and usage
│   ├── generate_test_data.py # Script to create test data
│   └── test_data/         # Generated test CSV files (gitignored)
├── build_scripts/         # Build and packaging scripts
│   ├── build_cross_platform.py # Cross-platform build script
│   ├── build_windows.bat  # Windows build script
│   ├── build_macos.sh     # macOS build script
│   └── pyinstaller_spec.py # PyInstaller configuration
├── main.py                # Main application entry point
├── setup.py              # Package setup script
├── pyproject.toml        # Modern Python project configuration
├── requirements.txt      # Project dependencies
├── MANIFEST.in          # Package manifest
├── CHANGELOG.md         # Version history
├── RELEASES.md          # Release information
├── README.md           # Quick start guide
└── .gitignore           # Git ignore rules
```

## Package Structure

### `src/csv_splitter/` - Main Package

#### Core Modules

- **`__init__.py`**: Package initialization, exports main classes
- **`config.py`**: Centralized configuration, constants, and settings
- **`exceptions.py`**: Custom exception hierarchy for error handling
- **`processor.py`**: Pure CSV processing logic, no UI dependencies
- **`gui.py`**: Main GUI application class and coordination logic
- **`ui_components.py`**: Reusable UI components and utilities
- **`logger.py`**: Logging configuration and GUI integration

### `tests/` - Test Suite

- **`__init__.py`**: Test package initialization
- **`test_modular_app.py`**: Comprehensive tests for modular architecture
- **`test_gui_functionality.py`**: GUI-specific functionality tests

### `docs/` - Documentation

- **`README.md`**: Main project documentation and user guide
- **`ARCHITECTURE.md`**: Detailed architecture and design documentation
- **`PROJECT_STRUCTURE.md`**: This file - project organization guide

### `examples/` - Examples and Sample Data

- **`test_data.csv`**: Sample CSV file for testing and demonstrations

### `legacy/` - Legacy Code

- **`tb_seperator.py`**: Original command-line implementation for reference

## File Purposes

### Configuration Files

- **`setup.py`**: Traditional Python package setup script
- **`pyproject.toml`**: Modern Python project configuration (PEP 518)
- **`requirements.txt`**: Project dependencies and development tools
- **`MANIFEST.in`**: Specifies additional files to include in distribution
- **`.gitignore`**: Git ignore patterns for version control

### Entry Points

- **`main.py`**: Primary entry point for the GUI application
- **`setup.py`**: Defines console and GUI script entry points

## Import Structure

### Internal Imports

```python
# Main package imports
from csv_splitter import CSVSplitterGUI, CSVProcessor, Config, Logger

# Specific module imports
from csv_splitter.processor import ProcessingResult
from csv_splitter.exceptions import ValidationError, ProcessingError
from csv_splitter.ui_components import FieldSelectionTable, LogDisplay
```

### Entry Point Usage

```python
# From main.py
from csv_splitter import CSVSplitterGUI, Logger

# From tests
from csv_splitter import CSVProcessor
from csv_splitter.processor import ProcessingResult
```

## Development Workflow

### Running the Application

```bash
# Direct execution
python main.py

# As installed package
pip install -e .
csv-splitter-gui
```

### Running Tests

```bash
# All tests
python -m pytest tests/

# Specific test files
python tests/test_modular_app.py
python tests/test_gui_functionality.py
```

### Development Tools

```bash
# Install development dependencies
pip install -r requirements.txt

# Code formatting
black src/ tests/
isort src/ tests/

# Type checking
mypy src/

# Linting
flake8 src/ tests/
```

## Design Principles

### 1. Separation of Concerns
- Each module has a single, well-defined responsibility
- UI logic separated from business logic
- Configuration centralized in dedicated module

### 2. Modularity
- Reusable components for common functionality
- Clear interfaces between modules
- Easy to test and maintain individual components

### 3. Extensibility
- Plugin-ready architecture
- Configuration-driven behavior
- Event-driven progress reporting

### 4. Maintainability
- Comprehensive documentation
- Type hints throughout
- Consistent coding standards
- Clear project organization

## Adding New Features

### 1. Core Processing Features
Add to `src/csv_splitter/processor.py`:
- Extend `CSVProcessor` class
- Add new processing methods
- Update `ProcessingResult` if needed

### 2. UI Features
Add to `src/csv_splitter/ui_components.py`:
- Create new component classes
- Follow existing patterns
- Integrate with main GUI in `gui.py`

### 3. Configuration
Add to `src/csv_splitter/config.py`:
- Add new constants or settings
- Use `Final` type annotations
- Group related settings together

### 4. Tests
Add to `tests/`:
- Create test files for new functionality
- Follow naming convention: `test_*.py`
- Use existing test patterns

## Package Distribution

### Building Distribution

```bash
# Build source and wheel distributions
python setup.py sdist bdist_wheel

# Or using build tool
pip install build
python -m build
```

### Installing from Source

```bash
# Development install
pip install -e .

# Regular install
pip install .
```

This structure provides a solid foundation for maintaining and extending the CSV Splitter GUI application while following Python packaging best practices.