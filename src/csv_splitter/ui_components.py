"""
UI components and utilities for the CSV Splitter GUI.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from typing import Dict, List, Optional, Callable
import os

from .config import Config


class FieldSelectionTable:
    """Manages the field selection table with split by and include checkboxes."""
    
    def __init__(self, parent_frame: ttk.Frame):
        self.parent_frame = parent_frame
        self.scrollable_frame: Optional[ttk.Frame] = None
        self.canvas: Optional[tk.Canvas] = None
        self.scrollbar: Optional[ttk.Scrollbar] = None
        self.split_by_vars: Dict[str, tk.BooleanVar] = {}
        self.include_vars: Dict[str, tk.BooleanVar] = {}
        
        self._setup_scrollable_frame()
    
    def _setup_scrollable_frame(self) -> None:
        """Set up the scrollable frame for the field table."""
        self.canvas = tk.Canvas(self.parent_frame, height=Config.FIELD_TABLE_HEIGHT)
        self.scrollbar = ttk.Scrollbar(self.parent_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )
        
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
    
    def update_fields(self, headers: List[str]) -> None:
        """Update the field selection table with new CSV headers."""
        self.clear()
        
        if not headers:
            return
        
        # Create table headers
        ttk.Label(
            self.scrollable_frame, 
            text="Field Name", 
            font=('TkDefaultFont', 9, 'bold')
        ).grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        
        ttk.Label(
            self.scrollable_frame, 
            text="Split By", 
            font=('TkDefaultFont', 9, 'bold')
        ).grid(row=0, column=1, padx=5, pady=2)
        
        ttk.Label(
            self.scrollable_frame, 
            text="Include in Output", 
            font=('TkDefaultFont', 9, 'bold')
        ).grid(row=0, column=2, padx=5, pady=2)
        
        # Create separator
        ttk.Separator(
            self.scrollable_frame, 
            orient='horizontal'
        ).grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), padx=5, pady=2)
        
        # Create field rows
        for i, header in enumerate(headers):
            row = i + 2
            
            # Field name label
            ttk.Label(
                self.scrollable_frame, 
                text=header
            ).grid(row=row, column=0, sticky=tk.W, padx=5, pady=1)
            
            # Split by checkbox
            split_by_var = tk.BooleanVar()
            self.split_by_vars[header] = split_by_var
            ttk.Checkbutton(
                self.scrollable_frame, 
                variable=split_by_var
            ).grid(row=row, column=1, padx=20, pady=1)
            
            # Include in output checkbox (default checked)
            include_var = tk.BooleanVar(value=True)
            self.include_vars[header] = include_var
            ttk.Checkbutton(
                self.scrollable_frame, 
                variable=include_var
            ).grid(row=row, column=2, padx=30, pady=1)
    
    def clear(self) -> None:
        """Clear all widgets and variables."""
        if self.scrollable_frame:
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()
        
        self.split_by_vars.clear()
        self.include_vars.clear()
    
    def get_split_by_fields(self) -> List[str]:
        """Get list of fields selected for splitting."""
        return [field for field, var in self.split_by_vars.items() if var.get()]
    
    def get_included_fields(self) -> List[str]:
        """Get list of fields selected for output."""
        return [field for field, var in self.include_vars.items() if var.get()]
    
    def select_all_split_by(self) -> None:
        """Select all split by checkboxes."""
        for var in self.split_by_vars.values():
            var.set(True)
    
    def clear_all_split_by(self) -> None:
        """Clear all split by checkboxes."""
        for var in self.split_by_vars.values():
            var.set(False)
    
    def select_all_fields(self) -> None:
        """Select all include field checkboxes."""
        for var in self.include_vars.values():
            var.set(True)
    
    def clear_all_fields(self) -> None:
        """Clear all include field checkboxes."""
        for var in self.include_vars.values():
            var.set(False)


class LogDisplay:
    """Manages the log display area."""
    
    def __init__(self, parent_frame: ttk.Frame):
        self.parent_frame = parent_frame
        self.log_text: Optional[tk.Text] = None
        self._setup_log_area()
    
    def _setup_log_area(self) -> None:
        """Set up the log display area."""
        log_frame = ttk.Frame(self.parent_frame)
        log_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        log_frame.columnconfigure(0, weight=1)
        log_frame.rowconfigure(0, weight=1)
        
        self.log_text = tk.Text(log_frame, height=Config.LOG_HEIGHT, wrap=tk.WORD)
        log_scrollbar = ttk.Scrollbar(log_frame, orient="vertical", command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=log_scrollbar.set)
        
        self.log_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        log_scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
    
    def add_message(self, message: str) -> None:
        """Add a message to the log display."""
        if self.log_text:
            self.log_text.insert(tk.END, message + "\n")
            self.log_text.see(tk.END)
    
    def clear(self) -> None:
        """Clear the log display."""
        if self.log_text:
            self.log_text.delete(1.0, tk.END)


class FileSelector:
    """Handles file and directory selection operations."""
    
    @staticmethod
    def select_csv_file(title: str = "Select CSV File") -> Optional[str]:
        """
        Open file dialog to select a CSV file.
        
        Args:
            title: Dialog title
            
        Returns:
            Selected file path or None if cancelled
        """
        return filedialog.askopenfilename(
            title=title,
            filetypes=Config.CSV_FILE_TYPES
        )
    
    @staticmethod
    def select_directory(title: str = "Select Directory") -> Optional[str]:
        """
        Open directory dialog to select an output directory.
        
        Args:
            title: Dialog title
            
        Returns:
            Selected directory path or None if cancelled
        """
        return filedialog.askdirectory(title=title)
    
    @staticmethod
    def get_default_output_dir(input_file_path: str) -> str:
        """
        Generate default output directory based on input file path.
        
        Args:
            input_file_path: Path to the input file
            
        Returns:
            Default output directory path
        """
        input_dir = os.path.dirname(input_file_path)
        input_filename = os.path.basename(input_file_path)
        input_name = os.path.splitext(input_filename)[0]
        return os.path.join(input_dir, input_name)


class ValidationHelper:
    """Helper class for input validation and error display."""
    
    @staticmethod
    def validate_inputs(
        input_file: str,
        output_dir: str, 
        split_by_fields: List[str],
        included_fields: List[str]
    ) -> bool:
        """
        Validate user inputs and show error messages if needed.
        
        Args:
            input_file: Path to input CSV file
            output_dir: Output directory path
            split_by_fields: List of split_by field names
            included_fields: List of included field names
            
        Returns:
            True if validation passes, False otherwise
        """
        if not input_file:
            messagebox.showerror("Error", Config.ERROR_NO_INPUT_FILE)
            return False
        
        if not os.path.exists(input_file):
            messagebox.showerror("Error", Config.ERROR_FILE_NOT_EXISTS)
            return False
        
        if not split_by_fields:
            messagebox.showerror("Error", Config.ERROR_NO_SPLIT_BY_FIELDS)
            return False
        
        if not included_fields:
            messagebox.showerror("Error", Config.ERROR_NO_INCLUDED_FIELDS)
            return False
        
        if not output_dir:
            messagebox.showerror("Error", Config.ERROR_NO_OUTPUT_DIR)
            return False
        
        return True
    
    @staticmethod
    def show_error(title: str, message: str) -> None:
        """Show error message dialog."""
        messagebox.showerror(title, message)
    
    @staticmethod
    def show_success(title: str, message: str) -> None:
        """Show success message dialog."""
        messagebox.showinfo(title, message)
    
    @staticmethod
    def show_processing_complete(files_created: int, total_rows: int) -> None:
        """Show processing completion message."""
        message = (f"{Config.SUCCESS_PROCESSING_COMPLETE}\n\n"
                  f"Files created: {files_created}\n"
                  f"Rows processed: {total_rows}")
        ValidationHelper.show_success("Success", message)