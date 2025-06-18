"""
Custom exceptions for CSV Splitter application.
"""


class CSVSplitterException(Exception):
    """Base exception class for CSV Splitter application."""
    pass


class ValidationError(CSVSplitterException):
    """Raised when input validation fails."""
    pass


class ProcessingError(CSVSplitterException):
    """Raised when CSV processing encounters an error."""
    pass


class FileOperationError(CSVSplitterException):
    """Raised when file operations fail."""
    pass