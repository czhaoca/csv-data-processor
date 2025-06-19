"""
Logging configuration for CSV Splitter application.
"""

import logging
import sys
from typing import Optional
from datetime import datetime

from .config import Config


class Logger:
    """Centralized logging configuration and management."""
    
    _instance: Optional['Logger'] = None
    _configured = False
    
    def __new__(cls) -> 'Logger':
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self):
        if not self._configured:
            self._setup_logging()
            self._configured = True
    
    def _setup_logging(self) -> None:
        """Configure application logging."""
        # Create formatter
        formatter = logging.Formatter(
            Config.LOG_FORMAT,
            datefmt=Config.LOG_DATE_FORMAT
        )
        
        # Create console handler
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        
        # Configure root logger
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.INFO)
        root_logger.addHandler(console_handler)
    
    @staticmethod
    def get_logger(name: str) -> logging.Logger:
        """
        Get a logger instance.
        
        Args:
            name: Logger name (typically __name__)
            
        Returns:
            Configured logger instance
        """
        # Ensure logging is configured
        Logger()
        return logging.getLogger(name)


class GUILogHandler(logging.Handler):
    """Custom logging handler that sends messages to GUI log display."""
    
    def __init__(self, log_callback):
        super().__init__()
        self.log_callback = log_callback
    
    def emit(self, record):
        """Emit a log record to the GUI."""
        try:
            message = self.format(record)
            if self.log_callback:
                self.log_callback(message)
        except Exception:
            self.handleError(record)


def setup_gui_logging(log_callback) -> None:
    """
    Set up logging to send messages to GUI log display.
    
    Args:
        log_callback: Function to call with log messages
    """
    # Create GUI handler
    gui_handler = GUILogHandler(log_callback)
    gui_handler.setLevel(logging.INFO)
    
    # Create formatter for GUI messages
    formatter = logging.Formatter(
        "[%(asctime)s] %(message)s",
        datefmt="%H:%M:%S"
    )
    gui_handler.setFormatter(formatter)
    
    # Add handler to CSV splitter loggers
    csv_logger = logging.getLogger('csv_splitter')
    csv_logger.addHandler(gui_handler)
    csv_logger.setLevel(logging.INFO)