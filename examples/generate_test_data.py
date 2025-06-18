#!/usr/bin/env python3
"""
Generate test CSV data for CSV Splitter GUI testing.

This script creates sample CSV files with various data patterns
to test the CSV Splitter functionality.
"""

import csv
from pathlib import Path


def create_test_data_directory():
    """Create test_data directory if it doesn't exist."""
    test_data_dir = Path(__file__).parent / "test_data"
    test_data_dir.mkdir(exist_ok=True)
    return test_data_dir


def generate_employee_data():
    """Generate sample employee data."""
    return [
        ['ID', 'NAME', 'DEPARTMENT', 'SALARY', 'LOCATION', 'STATUS'],
        ['1', 'John Doe', 'IT', '75000', 'New York', 'Active'],
        ['2', 'Jane Smith', 'HR', '65000', 'Los Angeles', 'Active'],
        ['3', 'Bob Johnson', 'IT', '80000', 'Chicago', 'Active'],
        ['4', 'Alice Brown', 'Finance', '70000', 'New York', 'Inactive'],
        ['5', 'Charlie Wilson', 'HR', '60000', 'Los Angeles', 'Active'],
        ['6', 'Diana Lee', 'Finance', '85000', 'Chicago', 'Active'],
        ['7', 'Edward Davis', 'IT', '72000', 'New York', 'Active'],
        ['8', 'Fiona Garcia', 'HR', '58000', 'Los Angeles', 'Inactive'],
        ['9', 'George Miller', 'Finance', '90000', 'Chicago', 'Active'],
        ['10', 'Helen Rodriguez', 'IT', '77000', 'New York', 'Active'],
    ]


def generate_sales_data():
    """Generate sample sales data."""
    return [
        ['ORDER_ID', 'CUSTOMER', 'PRODUCT', 'QUANTITY', 'REGION', 'SALES_REP'],
        ['ORD001', 'Acme Corp', 'Widget A', '100', 'North', 'Sarah Johnson'],
        ['ORD002', 'Beta Inc', 'Widget B', '75', 'South', 'Mike Chen'],
        ['ORD003', 'Gamma LLC', 'Widget A', '150', 'East', 'Sarah Johnson'],
        ['ORD004', 'Delta Co', 'Widget C', '50', 'West', 'Lisa Wang'],
        ['ORD005', 'Epsilon Ltd', 'Widget B', '200', 'North', 'Sarah Johnson'],
        ['ORD006', 'Zeta Corp', 'Widget A', '125', 'South', 'Mike Chen'],
        ['ORD007', 'Eta Inc', 'Widget C', '300', 'East', 'David Lee'],
        ['ORD008', 'Theta LLC', 'Widget B', '175', 'West', 'Lisa Wang'],
    ]


def generate_inventory_data():
    """Generate sample inventory data."""
    return [
        ['SKU', 'PRODUCT_NAME', 'CATEGORY', 'WAREHOUSE', 'STOCK_LEVEL', 'SUPPLIER'],
        ['SKU001', 'Laptop Pro', 'Electronics', 'Warehouse A', '45', 'TechCorp'],
        ['SKU002', 'Office Chair', 'Furniture', 'Warehouse B', '120', 'FurniCo'],
        ['SKU003', 'Wireless Mouse', 'Electronics', 'Warehouse A', '200', 'TechCorp'],
        ['SKU004', 'Standing Desk', 'Furniture', 'Warehouse C', '30', 'FurniCo'],
        ['SKU005', 'Smartphone', 'Electronics', 'Warehouse A', '85', 'MobileTech'],
        ['SKU006', 'Bookshelf', 'Furniture', 'Warehouse B', '60', 'WoodWorks'],
        ['SKU007', 'Tablet', 'Electronics', 'Warehouse C', '95', 'MobileTech'],
        ['SKU008', 'Desk Lamp', 'Furniture', 'Warehouse B', '150', 'LightCo'],
    ]


def write_csv_file(filename, data):
    """Write data to CSV file."""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quotechar='"', quoting=csv.QUOTE_ALL)
        writer.writerows(data)
    print(f"Generated: {filename}")


def main():
    """Generate all test data files."""
    print("Generating test data for CSV Splitter GUI...")
    
    # Create test data directory
    test_data_dir = create_test_data_directory()
    
    # Generate different types of test data
    datasets = [
        ("employee_data.csv", generate_employee_data()),
        ("sales_data.csv", generate_sales_data()),
        ("inventory_data.csv", generate_inventory_data()),
    ]
    
    for filename, data in datasets:
        filepath = test_data_dir / filename
        write_csv_file(filepath, data)
    
    print(f"\nTest data generated in: {test_data_dir}")
    print("\nUsage examples:")
    print("- employee_data.csv: Split by DEPARTMENT, LOCATION, or STATUS")
    print("- sales_data.csv: Split by REGION, SALES_REP, or PRODUCT")
    print("- inventory_data.csv: Split by CATEGORY, WAREHOUSE, or SUPPLIER")
    print("\nLoad any of these files in CSV Splitter GUI to test functionality!")


if __name__ == "__main__":
    main()