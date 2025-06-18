"""
Main GUI application for CSV Splitter.
"""

import tkinter as tk
from tkinter import ttk
import threading
from typing import Optional
from datetime import datetime

from .config import Config
from .processor import CSVProcessor
from .ui_components import (
    FieldSelectionTable, 
    LogDisplay, 
    FileSelector, 
    ValidationHelper
)
from .logger import Logger, setup_gui_logging
from .exceptions import CSVSplitterException


class CSVSplitterGUI:
    """Main GUI application class for CSV Splitter."""
    
    def __init__(self, root: tk.Tk):
        """
        Initialize the CSV Splitter GUI.
        
        Args:
            root: The main Tkinter window
        """
        self.root = root
        self.logger = Logger.get_logger(__name__)
        
        # Initialize variables
        self.input_file = tk.StringVar()
        self.output_dir = tk.StringVar()
        self.csv_headers = []
        
        # Initialize components
        self.processor = CSVProcessor(progress_callback=self._log_message)
        self.field_table: Optional[FieldSelectionTable] = None
        self.log_display: Optional[LogDisplay] = None
        self.progress: Optional[ttk.Progressbar] = None
        self.status_label: Optional[ttk.Label] = None
        
        # Setup GUI
        self._setup_window()
        self._setup_ui()
        self._setup_logging()
    
    def _setup_window(self) -> None:
        """Configure the main window."""
        self.root.title(Config.WINDOW_TITLE)
        self.root.geometry(Config.WINDOW_SIZE)
    
    def _setup_ui(self) -> None:
        """Set up the user interface."""
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        self._create_file_input_section(main_frame)
        self._create_field_selection_section(main_frame)
        self._create_output_section(main_frame)
        self._create_control_section(main_frame)
        self._create_log_section(main_frame)
        
        # Configure row weights for proper resizing
        main_frame.rowconfigure(1, weight=1)  # Field selection
        main_frame.rowconfigure(7, weight=1)  # Log section
    
    def _create_file_input_section(self, parent: ttk.Frame) -> None:
        """Create the file input section."""
        ttk.Label(parent, text="Input CSV File:").grid(
            row=0, column=0, sticky=tk.W, pady=5
        )
        ttk.Entry(parent, textvariable=self.input_file, width=50).grid(
            row=0, column=1, sticky=(tk.W, tk.E), padx=5
        )
        ttk.Button(parent, text="Browse", command=self._browse_input_file).grid(
            row=0, column=2, padx=5
        )
    
    def _create_field_selection_section(self, parent: ttk.Frame) -> None:
        """Create the field selection section."""
        ttk.Label(parent, text="Field Selection:").grid(
            row=1, column=0, sticky=(tk.W, tk.N), pady=5
        )
        
        field_frame = ttk.Frame(parent)
        field_frame.grid(
            row=1, column=1, columnspan=2, 
            sticky=(tk.W, tk.E, tk.N, tk.S), padx=5, pady=5
        )
        
        self.field_table = FieldSelectionTable(field_frame)
    
    def _create_output_section(self, parent: ttk.Frame) -> None:
        """Create the output directory selection section."""
        ttk.Label(parent, text="Output Directory:").grid(
            row=2, column=0, sticky=tk.W, pady=5
        )
        ttk.Entry(parent, textvariable=self.output_dir, width=50).grid(
            row=2, column=1, sticky=(tk.W, tk.E), padx=5
        )
        ttk.Button(parent, text="Browse", command=self._browse_output_dir).grid(
            row=2, column=2, padx=5
        )
    
    def _create_control_section(self, parent: ttk.Frame) -> None:
        """Create the control section with progress bar and buttons."""
        # Progress bar
        self.progress = ttk.Progressbar(parent, mode='indeterminate')
        self.progress.grid(
            row=3, column=0, columnspan=3, 
            sticky=(tk.W, tk.E), pady=10
        )
        
        # Status label
        self.status_label = ttk.Label(parent, text="Ready")
        self.status_label.grid(row=4, column=0, columnspan=3, pady=5)
        
        # Control buttons
        self._create_buttons(parent)
    
    def _create_buttons(self, parent: ttk.Frame) -> None:
        """Create control buttons."""
        button_frame = ttk.Frame(parent)
        button_frame.grid(row=5, column=0, columnspan=3, pady=10)
        
        # Main action buttons
        ttk.Button(
            button_frame, text="Process CSV", command=self._process_csv
        ).pack(side=tk.LEFT, padx=Config.BUTTON_PADDING)
        
        ttk.Button(
            button_frame, text="Clear", command=self._clear_form
        ).pack(side=tk.LEFT, padx=Config.BUTTON_PADDING)
        
        # Field selection helper buttons
        ttk.Separator(button_frame, orient='vertical').pack(
            side=tk.LEFT, fill='y', padx=10
        )
        
        ttk.Button(
            button_frame, text="Select All Groups", 
            command=self._select_all_groups
        ).pack(side=tk.LEFT, padx=Config.BUTTON_PADDING)
        
        ttk.Button(
            button_frame, text="Clear All Groups", 
            command=self._clear_all_groups
        ).pack(side=tk.LEFT, padx=Config.BUTTON_PADDING)
        
        ttk.Button(
            button_frame, text="Select All Fields", 
            command=self._select_all_fields
        ).pack(side=tk.LEFT, padx=Config.BUTTON_PADDING)
        
        ttk.Button(
            button_frame, text="Clear All Fields", 
            command=self._clear_all_fields
        ).pack(side=tk.LEFT, padx=Config.BUTTON_PADDING)
    
    def _create_log_section(self, parent: ttk.Frame) -> None:
        """Create the log display section."""
        ttk.Label(parent, text="Process Log:").grid(
            row=6, column=0, sticky=(tk.W, tk.N), pady=(10, 0)
        )
        
        log_frame = ttk.Frame(parent)
        log_frame.grid(
            row=7, column=0, columnspan=3, 
            sticky=(tk.W, tk.E, tk.N, tk.S), pady=5
        )
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
        self.log_display = LogDisplay(log_frame)
    
    def _setup_logging(self) -> None:
        """Set up logging to display in GUI."""
        setup_gui_logging(self._log_message)
    
    def _browse_input_file(self) -> None:
        """Handle input file selection."""
        filename = FileSelector.select_csv_file()
        if filename:
            self.input_file.set(filename)
            self._load_csv_headers()
            self._set_default_output_dir()
    
    def _browse_output_dir(self) -> None:
        """Handle output directory selection."""
        directory = FileSelector.select_directory()
        if directory:
            self.output_dir.set(directory)
    
    def _load_csv_headers(self) -> None:
        """Load CSV headers and update field selection table."""
        try:
            self.csv_headers = CSVProcessor.get_csv_headers(self.input_file.get())
            self.field_table.update_fields(self.csv_headers)
            self._log_message(f"Loaded {len(self.csv_headers)} fields from CSV file")
            
        except CSVSplitterException as e:
            ValidationHelper.show_error("Error", f"Failed to read CSV file: {str(e)}")
            self._log_message(f"Error loading CSV headers: {str(e)}")
    
    def _set_default_output_dir(self) -> None:
        """Set default output directory based on input file."""
        if self.input_file.get():
            default_output = FileSelector.get_default_output_dir(self.input_file.get())
            self.output_dir.set(default_output)
    
    def _clear_form(self) -> None:
        """Clear all form inputs and reset to initial state."""
        self.input_file.set("")
        self.output_dir.set("")
        self.csv_headers = []
        
        if self.field_table:
            self.field_table.clear()
        if self.log_display:
            self.log_display.clear()
        if self.status_label:
            self.status_label.config(text="Ready")
    
    def _select_all_groups(self) -> None:
        """Select all group by checkboxes."""
        if self.field_table:
            self.field_table.select_all_groups()
    
    def _clear_all_groups(self) -> None:
        """Clear all group by checkboxes."""
        if self.field_table:
            self.field_table.clear_all_groups()
    
    def _select_all_fields(self) -> None:
        """Select all include field checkboxes."""
        if self.field_table:
            self.field_table.select_all_fields()
    
    def _clear_all_fields(self) -> None:
        """Clear all include field checkboxes."""
        if self.field_table:
            self.field_table.clear_all_fields()
    
    def _log_message(self, message: str) -> None:
        """Add a timestamped message to the log display."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        
        if self.log_display:
            self.log_display.add_message(log_entry)
        
        # Update GUI to show new log message
        self.root.update_idletasks()
    
    def _validate_inputs(self) -> bool:
        """Validate user inputs before processing."""
        groupby_fields = self.field_table.get_groupby_fields() if self.field_table else []
        included_fields = self.field_table.get_included_fields() if self.field_table else []
        
        return ValidationHelper.validate_inputs(
            self.input_file.get(),
            self.output_dir.get(),
            groupby_fields,
            included_fields
        )
    
    def _process_csv(self) -> None:
        """Start CSV processing in a separate thread."""
        if not self._validate_inputs():
            return
        
        # Run processing in a separate thread to avoid blocking the GUI
        processing_thread = threading.Thread(target=self._process_csv_worker)
        processing_thread.daemon = True
        processing_thread.start()
    
    def _process_csv_worker(self) -> None:
        """Worker method for CSV processing (runs in separate thread)."""
        try:
            # Update UI state
            self.root.after(0, lambda: self.progress.start())
            self.root.after(0, lambda: self.status_label.config(text="Processing..."))
            
            # Get processing parameters
            source_file = self.input_file.get()
            output_dir = self.output_dir.get()
            groupby_fields = self.field_table.get_groupby_fields()
            included_fields = self.field_table.get_included_fields()
            
            # Log processing start
            self.root.after(0, lambda: self._log_message("Starting CSV processing"))
            self.root.after(0, lambda: self._log_message(f"Input file: {source_file}"))
            self.root.after(0, lambda: self._log_message(f"Output directory: {output_dir}"))
            self.root.after(0, lambda: self._log_message(f"Group by fields: {', '.join(groupby_fields)}"))
            self.root.after(0, lambda: self._log_message(f"Included fields: {', '.join(included_fields)}"))
            
            # Process the CSV file
            result = self.processor.split_csv_by_fields(
                source_file, output_dir, groupby_fields, included_fields
            )
            
            # Handle results
            if result.success:
                self.root.after(0, lambda: self._log_message("Processing completed successfully"))
                self.root.after(0, lambda: self._log_message(f"Created {result.files_created} files"))
                self.root.after(0, lambda: self._log_message(f"Processed {result.total_rows} rows"))
                self.root.after(0, lambda: self.status_label.config(text="Completed successfully"))
                self.root.after(0, lambda: ValidationHelper.show_processing_complete(
                    result.files_created, result.total_rows
                ))
            else:
                self.root.after(0, lambda: self._log_message(f"Processing failed: {result.error}"))
                self.root.after(0, lambda: self.status_label.config(text="Processing failed"))
                self.root.after(0, lambda: ValidationHelper.show_error(
                    "Error", f"Processing failed: {result.error}"
                ))
                
        except Exception as e:
            self.root.after(0, lambda: self._log_message(f"Unexpected error: {str(e)}"))
            self.root.after(0, lambda: self.status_label.config(text="Error occurred"))
            self.root.after(0, lambda: ValidationHelper.show_error(
                "Error", f"Unexpected error: {str(e)}"
            ))
        finally:
            self.root.after(0, lambda: self.progress.stop())