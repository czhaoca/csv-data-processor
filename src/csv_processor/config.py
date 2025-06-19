"""
Configuration and constants for CSV Splitter application.
"""

from typing import Final


class Config:
    """Application configuration and constants."""
    
    # GUI Configuration
    WINDOW_TITLE: Final[str] = "CSV Splitter"
    WINDOW_SIZE: Final[str] = "900x700"
    
    # CSV Processing Configuration
    DEFAULT_ENCODING: Final[str] = "utf-8"
    PROGRESS_UPDATE_INTERVAL: Final[int] = 1000  # Update progress every N rows
    
    # File Extensions
    CSV_EXTENSION: Final[str] = ".csv"
    SUPPORTED_EXTENSIONS: Final[tuple] = (".csv",)
    
    # UI Constants
    LOG_HEIGHT: Final[int] = 8
    FIELD_TABLE_HEIGHT: Final[int] = 200
    BUTTON_PADDING: Final[int] = 5
    
    # File Dialog Configuration
    CSV_FILE_TYPES: Final[tuple] = (
        ("CSV files", "*.csv"),
        ("All files", "*.*")
    )
    
    # Error Messages
    ERROR_NO_INPUT_FILE: Final[str] = "Please select an input CSV file"
    ERROR_FILE_NOT_EXISTS: Final[str] = "Input file does not exist"
    ERROR_NO_SPLIT_BY_FIELDS: Final[str] = "Please select at least one field to split by"
    ERROR_NO_OUTPUT_DIR: Final[str] = "Please specify an output directory"
    ERROR_NO_INCLUDED_FIELDS: Final[str] = "Please select at least one field to include in output"
    
    # Success Messages
    SUCCESS_PROCESSING_COMPLETE: Final[str] = "CSV processing completed successfully!"
    
    # Logging Configuration
    LOG_FORMAT: Final[str] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    LOG_DATE_FORMAT: Final[str] = "%Y-%m-%d %H:%M:%S"