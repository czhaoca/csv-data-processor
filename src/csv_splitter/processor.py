"""
CSV processing logic for splitting files based on field values.
"""

import csv
import os
import logging
from typing import List, Dict, Tuple, Any, Optional, Callable
from pathlib import Path

from .config import Config
from .exceptions import ProcessingError, FileOperationError, ValidationError


class ProcessingResult:
    """Data class for processing results."""
    
    def __init__(self, success: bool, files_created: int = 0, total_rows: int = 0, error: Optional[str] = None):
        self.success = success
        self.files_created = files_created
        self.total_rows = total_rows
        self.error = error
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for backward compatibility."""
        return {
            'success': self.success,
            'files_created': self.files_created,
            'total_rows': self.total_rows,
            'error': self.error
        }


class CSVProcessor:
    """Handles CSV file processing and splitting operations."""
    
    def __init__(self, progress_callback: Optional[Callable[[str], None]] = None):
        """
        Initialize CSV processor.
        
        Args:
            progress_callback: Optional callback function for progress updates
        """
        self.logger = logging.getLogger(__name__)
        self.progress_callback = progress_callback
    
    def split_csv_by_fields(
        self, 
        source_file: str, 
        output_dir: str, 
        groupby_fields: List[str], 
        included_fields: List[str]
    ) -> ProcessingResult:
        """
        Split CSV file based on groupby fields and include only specified fields.
        
        Args:
            source_file: Path to the source CSV file
            output_dir: Directory where output files will be created
            groupby_fields: List of field names to group by
            included_fields: List of field names to include in output files
            
        Returns:
            ProcessingResult object containing operation results
        """
        try:
            self._validate_inputs(source_file, output_dir, groupby_fields, included_fields)
            return self._process_csv_file(source_file, output_dir, groupby_fields, included_fields)
        
        except (ValidationError, ProcessingError, FileOperationError) as e:
            self.logger.error(f"CSV processing failed: {e}")
            return ProcessingResult(success=False, error=str(e))
        except Exception as e:
            self.logger.error(f"Unexpected error during CSV processing: {e}")
            return ProcessingResult(success=False, error=f"Unexpected error: {str(e)}")
    
    def _validate_inputs(
        self, 
        source_file: str, 
        output_dir: str, 
        groupby_fields: List[str], 
        included_fields: List[str]
    ) -> None:
        """Validate input parameters."""
        if not source_file or not os.path.exists(source_file):
            raise ValidationError("Source file does not exist or is not specified")
        
        if not output_dir:
            raise ValidationError("Output directory is not specified")
        
        if not groupby_fields:
            raise ValidationError("At least one groupby field must be specified")
        
        if not included_fields:
            raise ValidationError("At least one field must be included in output")
    
    def _process_csv_file(
        self, 
        source_file: str, 
        output_dir: str, 
        groupby_fields: List[str], 
        included_fields: List[str]
    ) -> ProcessingResult:
        """Process the CSV file and create grouped output files."""
        try:
            # Ensure output directory exists
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            
            # Read and process CSV file
            group_data, header = self._read_and_group_csv(source_file, groupby_fields, included_fields)
            
            # Write grouped data to files
            files_created = self._write_grouped_files(output_dir, group_data, header, groupby_fields)
            
            total_rows = sum(len(rows) for rows in group_data.values())
            
            self.logger.info(f"Processing completed: {files_created} files created, {total_rows} rows processed")
            return ProcessingResult(success=True, files_created=files_created, total_rows=total_rows)
            
        except Exception as e:
            raise ProcessingError(f"Error processing CSV file: {str(e)}")
    
    def _read_and_group_csv(
        self, 
        source_file: str, 
        groupby_fields: List[str], 
        included_fields: List[str]
    ) -> Tuple[Dict[Tuple, List[List[str]]], List[str]]:
        """Read CSV file and group data by specified fields."""
        group_data: Dict[Tuple, List[List[str]]] = {}
        total_rows = 0
        
        try:
            with open(source_file, 'r', newline='', encoding=Config.DEFAULT_ENCODING) as csvfile:
                reader = csv.reader(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
                
                # Read and validate header
                header = next(reader)
                self._validate_fields_in_header(header, groupby_fields, included_fields)
                
                # Get field indices
                groupby_indices = [header.index(field) for field in groupby_fields]
                included_indices = [header.index(field) for field in included_fields]
                
                # Create new header with only included fields
                new_header = [header[i] for i in included_indices]
                
                # Process each row
                for row in reader:
                    total_rows += 1
                    
                    # Create group key from groupby field values
                    group_key = tuple(row[i] for i in groupby_indices)
                    
                    # Initialize group if not exists
                    if group_key not in group_data:
                        group_data[group_key] = []
                    
                    # Create new row with only included fields
                    new_row = [row[i] for i in included_indices]
                    group_data[group_key].append(new_row)
                    
                    # Report progress periodically
                    if total_rows % Config.PROGRESS_UPDATE_INTERVAL == 0:
                        self._report_progress(f"Processed {total_rows} rows...")
                
                return group_data, new_header
                
        except FileNotFoundError:
            raise FileOperationError(f"Source file not found: {source_file}")
        except PermissionError:
            raise FileOperationError(f"Permission denied accessing file: {source_file}")
        except UnicodeDecodeError:
            raise ProcessingError(f"Unable to decode file {source_file}. Please ensure it's a valid CSV file with UTF-8 encoding.")
    
    def _validate_fields_in_header(
        self, 
        header: List[str], 
        groupby_fields: List[str], 
        included_fields: List[str]
    ) -> None:
        """Validate that all specified fields exist in the CSV header."""
        missing_groupby = [field for field in groupby_fields if field not in header]
        if missing_groupby:
            raise ValidationError(f"Groupby fields not found in CSV header: {', '.join(missing_groupby)}")
        
        missing_included = [field for field in included_fields if field not in header]
        if missing_included:
            raise ValidationError(f"Included fields not found in CSV header: {', '.join(missing_included)}")
    
    def _write_grouped_files(
        self, 
        output_dir: str, 
        group_data: Dict[Tuple, List[List[str]]], 
        header: List[str], 
        groupby_fields: List[str]
    ) -> int:
        """Write grouped data to separate CSV files."""
        files_created = 0
        
        for group_key, rows in group_data.items():
            try:
                filename = self._generate_filename(group_key, groupby_fields)
                output_file = os.path.join(output_dir, filename)
                
                with open(output_file, 'w', newline='', encoding=Config.DEFAULT_ENCODING) as csvfile:
                    writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
                    writer.writerow(header)
                    writer.writerows(rows)
                
                files_created += 1
                
                # Report file creation
                group_display = self._format_group_display(group_key, groupby_fields)
                self._report_progress(f"Created file for {group_display} with {len(rows)} rows")
                
            except Exception as e:
                raise FileOperationError(f"Error writing output file: {str(e)}")
        
        return files_created
    
    def _generate_filename(self, group_key: Tuple, groupby_fields: List[str]) -> str:
        """Generate a clean filename from group key values."""
        if len(group_key) == 1:
            filename_parts = [str(group_key[0])]
        else:
            filename_parts = [f"{groupby_fields[i]}_{group_key[i]}" for i in range(len(group_key))]
        
        # Clean filename parts to ensure valid filesystem names
        clean_parts = []
        for part in filename_parts:
            clean_part = "".join(c for c in str(part) if c.isalnum() or c in (' ', '-', '_')).rstrip()
            clean_parts.append(clean_part if clean_part else "empty")
        
        return "_".join(clean_parts) + Config.CSV_EXTENSION
    
    def _format_group_display(self, group_key: Tuple, groupby_fields: List[str]) -> str:
        """Format group key for display purposes."""
        return " + ".join([f"{groupby_fields[i]}='{group_key[i]}'" for i in range(len(group_key))])
    
    def _report_progress(self, message: str) -> None:
        """Report progress through callback if available."""
        if self.progress_callback:
            self.progress_callback(message)
        else:
            self.logger.info(message)
    
    @staticmethod
    def get_csv_headers(file_path: str) -> List[str]:
        """
        Extract headers from CSV file.
        
        Args:
            file_path: Path to the CSV file
            
        Returns:
            List of header field names
            
        Raises:
            FileOperationError: If file cannot be read
            ProcessingError: If CSV format is invalid
        """
        try:
            with open(file_path, 'r', newline='', encoding=Config.DEFAULT_ENCODING) as csvfile:
                reader = csv.reader(csvfile)
                headers = next(reader)
                return headers
        except FileNotFoundError:
            raise FileOperationError(f"File not found: {file_path}")
        except PermissionError:
            raise FileOperationError(f"Permission denied: {file_path}")
        except StopIteration:
            raise ProcessingError("CSV file is empty or has no headers")
        except Exception as e:
            raise ProcessingError(f"Error reading CSV headers: {str(e)}")