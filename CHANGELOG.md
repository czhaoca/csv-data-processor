# Changelog

All notable changes to the CSV Data Processor project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2025-06-18

### Changed
- **Improved Terminology**: Replaced confusing "group by" language with clearer "split by" throughout the application
  - Updated all variable names: `groupby_fields` → `split_by_fields`
  - Updated method names: `get_groupby_fields()` → `get_split_by_fields()`
  - Updated GUI labels: "Group By" → "Split By" 
  - Updated error messages and constants
  - Updated all documentation, comments, and help text
- **Enhanced User Experience**: The new terminology makes it immediately clear that the application splits CSV files into multiple files, rather than performing SQL-like grouping operations
- **Improved Output File Naming**: Enhanced filename convention to include original filename
  - Format: `SplitByValue1-SplitByValue2_OriginalFileName.csv`
  - Example: `Finance-Active_employeeList.csv` for file `employeeList.csv` split by Department='Finance' and Status='Active'

### Technical
- Maintained full backward compatibility of all functionality
- Updated comprehensive test suite with new terminology
- Updated all documentation files (README, USER_GUIDE, ARCHITECTURE)
- No breaking changes to public APIs

## [2.0.0] - 2025-06-18

### Added
- **Modular Architecture**: Complete refactoring into clean, modular components
- **Multi-field Splitting**: Support for splitting by multiple field combinations  
- **Flexible Field Selection**: Choose exactly which fields to include in output
- **Type Safety**: Comprehensive type hints throughout the codebase
- **Enhanced Error Handling**: Robust exception hierarchy with user-friendly messages
- **Comprehensive Logging**: Structured logging with GUI integration
- **Professional Project Structure**: Standard Python package layout
- **Development Tools**: Setup for testing, linting, and code formatting
- **Package Installation**: Support for pip installation and console scripts
- **Cross-platform Builds**: GitHub Actions workflow for Windows/macOS executables
- **Code Signing Support**: Ready for Windows code signing to eliminate SmartScreen warnings
- **PyInstaller Spec Files**: Proper build configurations for consistent executables

### Changed
- **Project Organization**: Reorganized into standard Python package structure
  - `src/csv_splitter/` - Main application package
  - `tests/` - Test suite with proper imports
  - `docs/` - Comprehensive documentation
  - `examples/` - Sample data and usage examples
  - `legacy/` - Original implementations for reference
- **GUI Interface**: Enhanced field selection with checkbox table interface
- **Processing Logic**: Memory-efficient algorithms for large file handling
- **Configuration**: Centralized configuration management
- **Documentation**: Complete rewrite with architecture details

### Improved
- **Maintainability**: Clear separation of concerns and modular design
- **Testability**: Isolated components enable comprehensive unit testing
- **Extensibility**: Plugin-ready architecture for future enhancements
- **User Experience**: More intuitive interface with better error messages
- **Performance**: Optimized processing for large CSV files
- **Cross-platform Compatibility**: Enhanced support for Windows, macOS, and Linux

### Deprecated
- **Monolithic GUI**: `csv_splitter_gui.py` moved to legacy (still functional)
- **Single-field Separation**: Replaced with flexible multi-field splitting

### Removed
- **Hardcoded Configuration**: Replaced with centralized configuration system
- **Mixed Concerns**: Separated UI logic from business logic
- **Inline Error Handling**: Replaced with structured exception system

### Fixed
- **Import Issues**: Clean import paths with proper package structure
- **Code Quality**: Resolved all linting and type checking issues
- **Memory Usage**: Optimized for processing large files
- **Error Reporting**: Better error messages and user feedback

### Security
- **Input Validation**: Enhanced validation for all user inputs
- **File Handling**: Safer file operations with proper error handling
- **Path Security**: Secure file path handling and validation

## [1.0.0] - Previous Version

### Added
- Basic CSV splitting functionality
- Simple GUI interface
- Command-line version for field-based splitting
- Basic error handling and logging

### Features
- Split CSV by any specified field
- Exclude specific fields from output
- Basic progress tracking
- File-based logging

---

## Migration Guide

### From v1.0.0 to v2.0.0

#### Breaking Changes
- Project structure completely reorganized
- Import paths changed for modular architecture
- GUI interface enhanced with new field selection system

#### Compatibility
- **Legacy CLI**: `legacy/tb_seperator.py` maintains original functionality
- **Main Entry Point**: Use `python main.py` instead of `python csv_splitter_gui.py`
- **Package Installation**: New option to install as proper Python package

#### New Features to Adopt
1. **Multi-field Splitting**: Use checkbox interface to select multiple splitting fields
2. **Field Selection**: Choose exactly which fields to include in output
3. **Enhanced Error Handling**: Better error messages and validation
4. **Progress Tracking**: Improved real-time progress updates

#### Recommended Upgrade Path
1. Backup existing workflows using v1.0.0
2. Test new functionality with sample data
3. Update any scripts to use new entry points
4. Take advantage of new multi-field capabilities

For detailed migration assistance, see the documentation in `docs/README.md`.