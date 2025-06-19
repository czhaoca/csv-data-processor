#!/usr/bin/env python3
"""
CSV Data Processor Application

A modular, user-friendly application for processing and manipulating CSV files according to user needs.
"""

import sys
import tkinter as tk
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from csv_processor import CSVProcessorGUI, Logger


def main():
    """Main entry point for the CSV Data Processor application."""
    try:
        # Initialize logging
        logger = Logger.get_logger(__name__)
        logger.info("Starting CSV Data Processor application")
        
        # Create and configure main window
        root = tk.Tk()
        
        # Initialize GUI application
        app = CSVProcessorGUI(root)
        
        # Start the GUI event loop
        logger.info("CSV Data Processor ready")
        root.mainloop()
        
    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        logger.info("CSV Data Processor application closed")


if __name__ == "__main__":
    main()