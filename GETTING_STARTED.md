# Getting Started with CSV Splitter GUI

Welcome to CSV Splitter GUI! This guide will help you get up and running quickly, whether you're an end user or a developer.

## 🚀 Quick Start for End Users

### Option 1: Download Standalone Executable (Recommended)
1. **Download** the appropriate version for your system:
   - Windows: `CSV-Splitter-GUI.exe`
   - macOS: `CSV Splitter GUI.app` 
   - Linux: `CSV-Splitter-GUI`

2. **Run** the application:
   - Windows: Double-click the `.exe` file
   - macOS: Drag to Applications folder, then open
   - Linux: Make executable and run: `chmod +x CSV-Splitter-GUI && ./CSV-Splitter-GUI`

3. **Start splitting CSV files!** 📊

### Option 2: Run from Source Code
```bash
# Clone the repository
git clone <repository-url>
cd csv-splitter-gui

# Generate test data (optional)
python examples/generate_test_data.py

# Run the application
python main.py
```

## 📖 How to Use CSV Splitter GUI

### Basic Workflow

1. **📁 Select Input File**
   - Click "Browse" next to "Input CSV File"
   - Choose your CSV file from your computer

2. **⚙️ Configure Field Selection**
   - **Group By**: Check the fields you want to use for splitting data
     - You can select multiple fields for complex grouping
   - **Include in Output**: Check which fields to include in the output files
     - All fields are selected by default

3. **📂 Choose Output Directory**
   - Click "Browse" next to "Output Directory"
   - Select where you want the split files to be saved
   - (Auto-suggests a folder based on your input file name)

4. **▶️ Process Your Data**
   - Click "Process CSV" to start splitting
   - Watch the progress bar and log messages for real-time updates

5. **✅ Done!**
   - Your split CSV files will be saved in the output directory
   - Each unique combination of your selected fields gets its own file

### Example Use Cases

#### Sales Data by Region
- **Input**: `sales_data.csv` with columns: Order, Customer, Product, Region, Sales_Rep
- **Group By**: Region ✓
- **Include**: Order, Customer, Product, Sales_Rep
- **Result**: Separate files for North.csv, South.csv, East.csv, West.csv

#### Employee Data by Department and Status
- **Input**: `employee_data.csv` with columns: ID, Name, Department, Salary, Location, Status
- **Group By**: Department ✓, Status ✓
- **Include**: ID, Name, Salary, Location
- **Result**: Files like `DEPARTMENT_IT_STATUS_Active.csv`, `DEPARTMENT_HR_STATUS_Active.csv`, etc.

## 🛠️ For Developers

### Development Setup

```bash
# Clone and enter directory
git clone <repository-url>
cd csv-splitter-gui

# Install development dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/

# Code formatting
black src/ tests/
isort src/ tests/

# Type checking
mypy src/
```

### Building Executables

```bash
# Auto-build for your platform
python build_scripts/build_cross_platform.py

# Platform-specific builds
python build_scripts/build_cross_platform.py  # Linux
bash build_scripts/build_macos.sh             # macOS  
build_scripts\build_windows.bat               # Windows
```

### Project Architecture

The application follows a clean, modular architecture:

- **`src/csv_splitter/`**: Core application modules
- **`tests/`**: Comprehensive test suite
- **`docs/`**: Detailed documentation
- **`examples/`**: Sample data generators
- **`build_scripts/`**: Build and packaging tools

## 📚 Need More Help?

### Documentation
- **[User Guide](docs/USER_GUIDE.md)**: Comprehensive feature documentation
- **[Architecture](docs/ARCHITECTURE.md)**: Technical details for developers
- **[Build Instructions](docs/BUILD_INSTRUCTIONS.md)**: Creating executables
- **[Project Structure](docs/PROJECT_STRUCTURE.md)**: Code organization

### Test Data
Generate sample data to experiment with:
```bash
python examples/generate_test_data.py
```

This creates three types of test data:
- **Employee data**: Test department/location grouping
- **Sales data**: Test region/product grouping  
- **Inventory data**: Test category/warehouse grouping

### Common Issues

#### "No module named 'tkinter'" (Linux)
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora/CentOS
sudo yum install tkinter
```

#### Large CSV Files
- The application handles large files efficiently
- Progress updates show processing status
- Processing runs in background (GUI stays responsive)

#### File Permissions (macOS)
If you get "damaged" warnings:
1. Right-click the app → Open
2. Or: System Preferences → Security → Allow

## 🎯 Tips for Best Results

### File Preparation
- ✅ Ensure your CSV has clear column headers
- ✅ Use consistent data formatting
- ✅ Check for special characters in field values

### Field Selection Strategy
- **Group By**: Choose fields that create meaningful data segments
- **Include**: Remove sensitive or unnecessary fields
- **Multiple Groups**: Combine fields for complex categorization

### Output Organization
- Use descriptive output directory names
- Consider grouping related splits in subfolders
- Keep original files as backups

## 🚀 Ready to Start?

1. **End Users**: Download your platform's executable and start splitting!
2. **Developers**: Clone the repository and explore the modular architecture
3. **Contributors**: Check the documentation and contribution guidelines

Happy CSV splitting! 📊✨

---

**Need support?** Check the project documentation or create an issue in the repository.