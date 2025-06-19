"""
CSV Data Processor Package

A modular CSV data processing application with GUI interface.
"""

__version__ = "2.0.0"
__author__ = "CSV Data Processor Team"

from .config import Config
from .processor import CSVProcessor
from .gui import CSVProcessorGUI
from .logger import Logger

__all__ = ["Config", "CSVProcessor", "CSVProcessorGUI", "Logger"]