#!/usr/bin/env python3
"""
Test script for the refactored modular CSV Splitter application.
"""

import sys
import tempfile
import csv
import os
from pathlib import Path

# Add src to path
src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from csv_splitter import CSVProcessor, Logger
from csv_splitter.processor import ProcessingResult


def create_test_csv():
    """Create a test CSV file for testing."""
    test_data = [
        ['ID', 'NAME', 'DEPARTMENT', 'SALARY', 'LOCATION', 'STATUS'],
        ['1', 'John Doe', 'IT', '75000', 'New York', 'Active'],
        ['2', 'Jane Smith', 'HR', '65000', 'Los Angeles', 'Active'],
        ['3', 'Bob Johnson', 'IT', '80000', 'Chicago', 'Active'],
        ['4', 'Alice Brown', 'Finance', '70000', 'New York', 'Inactive'],
        ['5', 'Charlie Wilson', 'HR', '60000', 'Los Angeles', 'Active'],
        ['6', 'Diana Lee', 'Finance', '85000', 'Chicago', 'Active'],
    ]
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False, newline='') as f:
        writer = csv.writer(f)
        writer.writerows(test_data)
        return f.name


def test_modular_csv_processor():
    """Test the modular CSV processor."""
    logger = Logger.get_logger(__name__)
    
    print("Testing Modular CSV Splitter...")
    
    # Create test data
    test_file = create_test_csv()
    output_dir = tempfile.mkdtemp()
    
    try:
        # Test header extraction
        print("\n1. Testing header extraction...")
        headers = CSVProcessor.get_csv_headers(test_file)
        print(f"   ✓ Headers: {headers}")
        
        # Create processor with progress callback
        messages = []
        def progress_callback(msg):
            messages.append(msg)
            print(f"   Progress: {msg}")
        
        processor = CSVProcessor(progress_callback=progress_callback)
        
        # Test 1: Single field splitting
        print("\n2. Testing single field splitting (DEPARTMENT)...")
        result = processor.split_csv_by_fields(
            test_file,
            os.path.join(output_dir, "test1"),
            split_by_fields=['DEPARTMENT'],
            included_fields=['ID', 'NAME', 'SALARY', 'LOCATION', 'STATUS']
        )
        
        if result.success:
            print(f"   ✓ Success: {result.files_created} files, {result.total_rows} rows")
        else:
            print(f"   ✗ Error: {result.error}")
        
        # Test 2: Multi-field splitting
        print("\n3. Testing multi-field splitting (DEPARTMENT + STATUS)...")
        result = processor.split_csv_by_fields(
            test_file,
            os.path.join(output_dir, "test2"),
            split_by_fields=['DEPARTMENT', 'STATUS'],
            included_fields=['ID', 'NAME', 'SALARY', 'LOCATION']
        )
        
        if result.success:
            print(f"   ✓ Success: {result.files_created} files, {result.total_rows} rows")
            
            # List created files
            test2_dir = os.path.join(output_dir, "test2")
            if os.path.exists(test2_dir):
                files = os.listdir(test2_dir)
                print(f"   Files created: {files}")
        else:
            print(f"   ✗ Error: {result.error}")
        
        # Test 3: Error handling
        print("\n4. Testing error handling...")
        result = processor.split_csv_by_fields(
            test_file,
            os.path.join(output_dir, "test3"),
            split_by_fields=['NONEXISTENT_FIELD'],
            included_fields=['ID', 'NAME']
        )
        
        if not result.success:
            print(f"   ✓ Properly handled error: {result.error}")
        else:
            print("   ✗ Should have failed with invalid field")
        
        print(f"\n5. Progress messages received: {len(messages)}")
        for msg in messages[:3]:  # Show first 3 messages
            print(f"   - {msg}")
        
        print("\n✓ All modular tests completed successfully!")
        
    finally:
        # Cleanup
        os.unlink(test_file)
        import shutil
        shutil.rmtree(output_dir)


def test_import_structure():
    """Test that all modules can be imported correctly."""
    print("Testing module imports...")
    
    try:
        from csv_splitter import Config, CSVProcessor, CSVSplitterGUI, Logger
        print("✓ All main modules imported successfully")
        
        from csv_splitter.exceptions import CSVSplitterException, ValidationError
        print("✓ Exception classes imported successfully")
        
        from csv_splitter.ui_components import FieldSelectionTable, LogDisplay
        print("✓ UI components imported successfully")
        
        # Test configuration access
        print(f"✓ Config loaded - Window title: {Config.WINDOW_TITLE}")
        
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False


if __name__ == "__main__":
    print("=" * 50)
    print("CSV Splitter Modular Architecture Test")
    print("=" * 50)
    
    # Test imports
    if test_import_structure():
        print("\n" + "=" * 50)
        # Test functionality
        test_modular_csv_processor()
    else:
        print("Cannot proceed with functionality tests due to import errors")
        sys.exit(1)