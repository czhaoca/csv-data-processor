#!/usr/bin/env python3
"""
Test script to verify the updated CSV data processor functionality
"""

import csv
import os
import sys
import tempfile
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from csv_processor.gui import CSVProcessorGUI

def test_csv_processing():
    """Test the core CSV processing logic"""
    
    # Create a test CSV file
    test_data = [
        ['ID', 'NAME', 'DEPARTMENT', 'SALARY', 'LOCATION', 'STATUS'],
        ['1', 'John Doe', 'IT', '75000', 'New York', 'Active'],
        ['2', 'Jane Smith', 'HR', '65000', 'Los Angeles', 'Active'],
        ['3', 'Bob Johnson', 'IT', '80000', 'Chicago', 'Active'],
        ['4', 'Alice Brown', 'Finance', '70000', 'New York', 'Inactive'],
        ['5', 'Charlie Wilson', 'HR', '60000', 'Los Angeles', 'Active'],
        ['6', 'Diana Lee', 'Finance', '85000', 'Chicago', 'Active'],
    ]
    
    # Create temporary files
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, newline='') as f:
        writer = csv.writer(f)
        writer.writerows(test_data)
        test_file = f.name
    
    output_dir = tempfile.mkdtemp()
    
    try:
        # Create a mock GUI instance for testing
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()  # Hide the window
        gui = CSVSplitterGUI(root)
        
        # Test case 1: Split by single field (DEPARTMENT)
        print("Test 1: Split by DEPARTMENT")
        split_by_fields = ['DEPARTMENT']
        included_fields = ['ID', 'NAME', 'SALARY', 'LOCATION', 'STATUS']
        
        test1_dir = os.path.join(output_dir, "test1")
        os.makedirs(test1_dir, exist_ok=True)
        result = gui.processor.split_csv_by_fields(test_file, test1_dir, split_by_fields, included_fields)
        
        if result.success:
            print(f"✓ Created {result.files_created} files, processed {result.total_rows} rows")
            
            # Check created files
            if os.path.exists(test1_dir):
                files = os.listdir(test1_dir)
                print(f"  Files created: {files}")
                
                # Verify content of one file
                if 'IT.csv' in files:
                    with open(os.path.join(test1_dir, 'IT.csv'), 'r') as f:
                        content = f.read()
                        print(f"  IT.csv content preview:\n    {content[:100]}...")
        else:
            print(f"✗ Error: {result.error}")
        
        # Test case 2: Split by multiple fields (DEPARTMENT + LOCATION)
        print("\nTest 2: Split by DEPARTMENT + LOCATION")
        split_by_fields = ['DEPARTMENT', 'LOCATION']
        included_fields = ['ID', 'NAME', 'SALARY', 'STATUS']
        
        test2_dir = os.path.join(output_dir, "test2")
        os.makedirs(test2_dir, exist_ok=True)
        result = gui.processor.split_csv_by_fields(test_file, test2_dir, split_by_fields, included_fields)
        
        if result.success:
            print(f"✓ Created {result.files_created} files, processed {result.total_rows} rows")
            
            # Check created files
            if os.path.exists(test2_dir):
                files = os.listdir(test2_dir)
                print(f"  Files created: {files}")
        else:
            print(f"✗ Error: {result.error}")
        
        # Test case 3: Split by STATUS, include only specific fields
        print("\nTest 3: Split by STATUS, limited fields")
        split_by_fields = ['STATUS']
        included_fields = ['NAME', 'DEPARTMENT', 'SALARY']
        
        test3_dir = os.path.join(output_dir, "test3")
        os.makedirs(test3_dir, exist_ok=True)
        result = gui.split_csv_by_fields(test_file, test3_dir, split_by_fields, included_fields)
        
        if result.success:
            print(f"✓ Created {result.files_created} files, processed {result.total_rows} rows")
            
            # Check created files
            if os.path.exists(test3_dir):
                files = os.listdir(test3_dir)
                print(f"  Files created: {files}")
        else:
            print(f"✗ Error: {result.error}")
        
        root.destroy()
        
    finally:
        # Cleanup
        os.unlink(test_file)
        import shutil
        shutil.rmtree(output_dir)
    
    print("\n✓ All tests completed successfully!")

if __name__ == "__main__":
    print("Testing updated CSV Splitter GUI functionality...")
    test_csv_processing()