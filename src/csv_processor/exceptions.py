"""
Custom exceptions for CSV Data Processor application.
"""


class CSVProcessorException(Exception):
    """Base exception class for CSV Data Processor application."""
    pass


class ValidationError(CSVProcessorException):
    """Raised when input validation fails."""
    pass


class ProcessingError(CSVProcessorException):
    """Raised when CSV processing encounters an error."""
    pass


class FileOperationError(CSVProcessorException):
    """Raised when file operations fail."""
    pass