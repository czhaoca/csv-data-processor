#!/usr/bin/env python3
"""
CSV Splitter GUI Application

A modular, user-friendly application for splitting CSV files based on field values.
"""

import sys
import tkinter as tk
from pathlib import Path

# Add src directory to Python path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from csv_splitter import CSVSplitterGUI, Logger


def main():
    """Main entry point for the CSV Splitter GUI application."""
    try:
        # Initialize logging
        logger = Logger.get_logger(__name__)
        logger.info("Starting CSV Splitter GUI application")
        
        # Create and configure main window
        root = tk.Tk()
        
        # Initialize GUI application
        app = CSVSplitterGUI(root)
        
        # Start the GUI event loop
        logger.info("CSV Splitter GUI ready")
        root.mainloop()
        
    except KeyboardInterrupt:
        logger.info("Application interrupted by user")
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
    finally:
        logger.info("CSV Splitter GUI application closed")


if __name__ == "__main__":
    main()