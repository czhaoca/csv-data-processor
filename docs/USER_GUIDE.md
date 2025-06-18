# CSV Splitter GUI

A modern, modular Python GUI application for splitting CSV files based on user-selected criteria. Built with clean architecture principles, this tool provides an intuitive interface for advanced CSV data manipulation and organization.

## Overview

This application enables users to split large CSV files into multiple organized files based on field values. With its flexible grouping system and field selection capabilities, it's perfect for data analysis, reporting workflows, and batch processing scenarios.

## Features

### Core Functionality
- **Multi-field grouping**: Group data by single or multiple field combinations
- **Flexible field selection**: Choose exactly which fields to include in output files
- **Advanced CSV processing**: Handles large files with memory-efficient algorithms
- **Robust error handling**: Comprehensive validation and error reporting

### User Experience
- **Intuitive GUI**: Clean, modern interface built with tkinter
- **Real-time feedback**: Live progress tracking and detailed logging
- **File browser integration**: Built-in file and directory selection dialogs
- **Batch operations**: Helper buttons for bulk field selection

### Technical Excellence
- **Modular architecture**: Clean separation of concerns with dedicated modules
- **Type safety**: Full type hints for better code reliability
- **Comprehensive logging**: Structured logging with multiple output targets
- **Threaded processing**: Non-blocking operations to maintain UI responsiveness
- **Cross-platform compatibility**: Works on Windows, macOS, and Linux

## Requirements

### System Requirements
- Python 3.7 or higher
- tkinter (included with most Python installations)
- Sufficient memory for processing large CSV files

### Dependencies
- **Runtime**: Uses only Python standard library (no external dependencies)
- **Development**: See `requirements.txt` for development and testing tools

## Installation & Usage

### Quick Start

1. **Clone or download the application**:
   ```bash
   git clone <repository-url>
   cd csv-splitter-gui
   ```

2. **Install dependencies (optional - only for development)**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the GUI application**:
   ```bash
   python main.py
   ```

### Alternative Installation Methods

**Install as a package**:
```bash
pip install -e .
csv-splitter-gui
```

**Legacy Command Line (original version)**:
```bash
python legacy/tb_seperator.py <source_csv_file>
```

## User Guide

### Application Workflow

1. **Select Input File**: Click "Browse" to choose your CSV file
2. **Configure Field Selection**:
   - **Group By**: Check fields to use for data grouping (supports multiple fields)
   - **Include in Output**: Check fields to include in output files (all selected by default)
3. **Set Output Directory**: Choose destination folder (auto-suggests based on input file)
4. **Process Data**: Click "Process CSV" to start the operation
5. **Monitor Progress**: Track progress through the status bar and detailed logs

### Helper Features

- **Bulk Selection**: Use "Select All" / "Clear All" buttons for quick field management
- **Smart Defaults**: Output directory and field selections are intelligently suggested
- **Real-time Validation**: Input validation with helpful error messages
- **Progress Tracking**: Live updates during processing with row counts and file creation status

## Output Structure

The GUI version creates the following output structure:

```
output_directory/
├── FieldValue1.csv
├── FieldValue2.csv
├── FieldValue3.csv
├── ...
└── [Additional files based on unique field values]
```

The legacy command-line version creates:

```
source_directory/
├── source_file.csv
└── source_file/                          # Output directory
    ├── VALUE1-split_output.csv
    ├── VALUE2-split_output.csv
    ├── ...
    └── source_file_process.log            # Processing log
```

## Processing Details

### Input Requirements

- CSV files with properly formatted headers
- Consistent field delimiters
- UTF-8 encoding recommended
- Any field can be used for separation (not limited to specific columns)

### Field Selection

- **Separation Field**: Choose any field from the CSV header to split data by
- **Field Exclusion**: Select multiple fields to exclude from output files
- **Dynamic Headers**: Output files automatically adjust headers based on exclusions

### Output Files

- Each unique value in the separation field gets its own CSV file
- Files are named using clean versions of the field values
- All files include the same header (minus excluded fields)
- Proper CSV quoting is maintained throughout processing

## GUI Features

### Real-time Feedback
- Progress bar shows processing status
- Live log updates during operation
- Status messages for each step
- Success/error notifications

### User-Friendly Interface
- File browser dialogs for easy selection
- Scrollable field lists for large CSV files
- Clear form functionality to reset all inputs
- Responsive design that works on different screen sizes

## Error Handling

The application includes comprehensive error handling for:
- Invalid file selections
- Missing required inputs
- CSV parsing errors
- File I/O issues
- Processing interruptions

## Use Cases

This tool is particularly useful for:
- Data analysis and reporting workflows
- Segregating data by categories or entities
- Preparing data for specialized processing
- Batch processing of large datasets
- Converting single files into organized datasets

## Architecture & Design

### Modular Structure

```
src/csv_splitter/
├── __init__.py          # Package initialization
├── config.py            # Configuration and constants
├── exceptions.py        # Custom exception classes
├── processor.py         # Core CSV processing logic
├── gui.py              # Main GUI application
├── ui_components.py    # Reusable UI components
└── logger.py           # Logging configuration
```

### Key Design Principles

- **Separation of Concerns**: Each module has a single, well-defined responsibility
- **Type Safety**: Comprehensive type hints for better code reliability
- **Error Handling**: Robust exception handling with user-friendly messages
- **Testability**: Modular design enables comprehensive unit testing
- **Maintainability**: Clean code structure with extensive documentation

### Technical Features

- **Memory Efficiency**: Processes large files without loading entire dataset into memory
- **Thread Safety**: GUI operations are properly isolated from processing logic
- **Cross-Platform**: Works consistently across Windows, macOS, and Linux
- **Extensibility**: Modular design allows easy addition of new features

## Development

### Setting Up Development Environment

1. **Install development dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run tests**:
   ```bash
   pytest
   ```

3. **Code formatting**:
   ```bash
   black src/
   isort src/
   ```

4. **Type checking**:
   ```bash
   mypy src/
   ```

### Testing

The application includes comprehensive tests:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src/csv_splitter

# Test specific functionality
python test_gui_functionality.py
```

### Contributing

When contributing to this project:

1. Follow the established modular architecture
2. Add type hints to all new functions
3. Include comprehensive docstrings
4. Write tests for new functionality
5. Ensure code passes all quality checks

## License

This project is provided as-is for data processing and educational purposes.