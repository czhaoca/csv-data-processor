# CSV Splitter GUI - Architecture Documentation

## Overview

The CSV Splitter GUI has been refactored from a monolithic application into a clean, modular architecture following software engineering best practices. This document outlines the design decisions, module structure, and benefits of the new architecture.

## Design Principles

### 1. Separation of Concerns
Each module has a single, well-defined responsibility:
- **Processing**: Pure CSV logic without UI dependencies
- **UI**: Interface components without business logic
- **Configuration**: Centralized settings and constants
- **Logging**: Structured logging across the application

### 2. Dependency Injection
- Components receive dependencies through constructor injection
- Enables easy testing and mocking
- Reduces tight coupling between modules

### 3. Type Safety
- Comprehensive type hints throughout the codebase
- Custom data classes for structured return values
- Enhanced IDE support and early error detection

### 4. Error Handling
- Custom exception hierarchy for different error types
- Graceful degradation with user-friendly error messages
- Proper logging of errors for debugging

## Module Structure

```
src/csv_splitter/
├── __init__.py          # Package initialization and exports
├── config.py            # Application configuration and constants
├── exceptions.py        # Custom exception classes
├── processor.py         # Core CSV processing logic
├── gui.py              # Main GUI application class
├── ui_components.py    # Reusable UI components
└── logger.py           # Logging configuration and utilities
```

### Core Modules

#### `config.py`
- Centralized configuration management
- Type-safe constants using `Final` annotations
- UI dimensions, file types, error messages
- Easy to modify without touching business logic

#### `exceptions.py`
- Custom exception hierarchy
- Specific exception types for different error scenarios
- Enables precise error handling and user feedback

#### `processor.py`
- Pure CSV processing logic
- `CSVProcessor` class with progress callback support
- `ProcessingResult` data class for structured return values
- Memory-efficient processing for large files
- Comprehensive input validation

#### `gui.py`
- Main GUI application class
- Coordinates between UI components and processing logic
- Threaded processing to maintain UI responsiveness
- Clean separation between UI and business logic

#### `ui_components.py`
- Reusable UI components
- `FieldSelectionTable`: Manages the field selection interface
- `LogDisplay`: Handles log message display
- `FileSelector`: File and directory selection utilities
- `ValidationHelper`: Input validation and error display

#### `logger.py`
- Centralized logging configuration
- Singleton pattern for consistent setup
- GUI log handler for displaying messages in the interface
- Structured logging with proper formatting

## Key Improvements

### 1. Maintainability
- **Modular Structure**: Easy to locate and modify specific functionality
- **Clear Interfaces**: Well-defined APIs between modules
- **Documentation**: Comprehensive docstrings and type hints
- **Single Responsibility**: Each class has one clear purpose

### 2. Testability
- **Pure Functions**: Business logic separated from UI
- **Dependency Injection**: Easy to mock dependencies
- **Error Scenarios**: Comprehensive error handling testing
- **Isolated Components**: Each module can be tested independently

### 3. Extensibility
- **Plugin Architecture**: Easy to add new processing algorithms
- **UI Components**: Reusable components for consistent interface
- **Configuration-Driven**: Behavior controlled through config
- **Event-Driven**: Progress callbacks for flexible monitoring

### 4. Reliability
- **Type Safety**: Comprehensive type checking
- **Input Validation**: Robust validation at all entry points
- **Error Recovery**: Graceful handling of unexpected conditions
- **Resource Management**: Proper cleanup and memory management

## Usage Patterns

### Processing CSV Files
```python
from csv_splitter import CSVProcessor

def progress_callback(message):
    print(f"Progress: {message}")

processor = CSVProcessor(progress_callback=progress_callback)
result = processor.split_csv_by_fields(
    source_file="data.csv",
    output_dir="output/",
    groupby_fields=["Department", "Status"],
    included_fields=["ID", "Name", "Salary"]
)

if result.success:
    print(f"Created {result.files_created} files")
else:
    print(f"Error: {result.error}")
```

### Custom UI Components
```python
from csv_splitter.ui_components import FieldSelectionTable

# Create field selection table
field_table = FieldSelectionTable(parent_frame)
field_table.update_fields(csv_headers)

# Get user selections
groupby_fields = field_table.get_groupby_fields()
included_fields = field_table.get_included_fields()
```

### Configuration Management
```python
from csv_splitter import Config

# Access configuration values
window_title = Config.WINDOW_TITLE
max_rows = Config.PROGRESS_UPDATE_INTERVAL
error_message = Config.ERROR_NO_INPUT_FILE
```

## Migration from Legacy Code

The refactoring maintains backward compatibility while providing the new modular benefits:

1. **Legacy GUI**: `csv_splitter_gui.py` still works for existing users
2. **New Entry Point**: `main.py` uses the modular architecture
3. **CLI Support**: Original `tb_seperator.py` remains available
4. **API Compatibility**: Core functionality accessible through clean APIs

## Future Enhancements

The modular architecture enables easy addition of new features:

1. **Export Formats**: Add JSON, Excel, XML output support
2. **Data Validation**: Field validation rules and data cleaning
3. **Scheduling**: Batch processing with scheduling capabilities
4. **Plugins**: Custom processing algorithms through plugin system
5. **Cloud Integration**: Support for cloud storage and processing

## Testing Strategy

The modular design enables comprehensive testing:

1. **Unit Tests**: Each module tested independently
2. **Integration Tests**: Component interaction testing
3. **UI Tests**: Interface behavior validation
4. **Performance Tests**: Large file processing benchmarks
5. **Error Handling Tests**: Robustness under error conditions

## Conclusion

The refactored CSV Splitter GUI demonstrates modern Python development practices:

- **Clean Architecture**: Modular, maintainable, and extensible
- **Type Safety**: Comprehensive type hints for reliability
- **Error Handling**: Robust error management and user feedback
- **Documentation**: Clear documentation and examples
- **Testing**: Testable design with isolated components

This architecture provides a solid foundation for future development while maintaining the simplicity and effectiveness of the original application.