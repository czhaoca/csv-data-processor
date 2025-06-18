"""
CSV Splitter Package

A modular CSV splitting application with GUI interface.
"""

__version__ = "2.0.0"
__author__ = "CSV Splitter Team"

from .config import Config
from .processor import CSVProcessor
from .gui import CSVSplitterGUI
from .logger import Logger

__all__ = ["Config", "CSVProcessor", "CSVSplitterGUI", "Logger"]