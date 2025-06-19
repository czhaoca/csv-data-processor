#!/usr/bin/env python3
"""
Cross-platform build script for CSV Data Processor.
Detects the current platform and runs the appropriate build process.
"""

import sys
import platform
import subprocess
import shutil
from pathlib import Path


def detect_platform():
    """Detect the current platform."""
    system = platform.system().lower()
    if system == "windows":
        return "windows"
    elif system == "darwin":
        return "macos"
    elif system == "linux":
        return "linux"
    else:
        return "unknown"


def check_dependencies():
    """Check if required build dependencies are installed."""
    required_modules = ["PyInstaller"]
    missing = []
    
    for module in required_modules:
        try:
            __import__(module.lower().replace("-", "_"))
        except ImportError:
            missing.append(module)
    
    if missing:
        print(f"Missing dependencies: {', '.join(missing)}")
        print("Installing missing dependencies...")
        subprocess.run([sys.executable, "-m", "pip", "install"] + missing)
        return True
    return False


def build_windows():
    """Build Windows executable."""
    print("Building for Windows...")
    build_script = Path(__file__).parent / "build_windows.bat"
    
    if not build_script.exists():
        print("Windows build script not found!")
        return False
    
    try:
        result = subprocess.run([str(build_script)], shell=True, check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        print("Windows build failed!")
        return False


def build_macos():
    """Build macOS application."""
    print("Building for macOS...")
    build_script = Path(__file__).parent / "build_macos.sh"
    
    if not build_script.exists():
        print("macOS build script not found!")
        return False
    
    try:
        result = subprocess.run(["bash", str(build_script)], check=True)
        return result.returncode == 0
    except subprocess.CalledProcessError:
        print("macOS build failed!")
        return False


def build_linux():
    """Build Linux executable."""
    print("Building for Linux...")
    
    # Clean previous builds
    dist_dir = Path("dist")
    build_dir = Path("build")
    
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
    if build_dir.exists():
        shutil.rmtree(build_dir)
    
    # PyInstaller command for Linux
    cmd = [
        "pyinstaller",
        "--clean",
        "--onefile",
        "--windowed",
        "--name", "CSV-Data-Processor",
        "--add-data", "src/csv_processor:csv_processor",
        "--hidden-import", "csv_processor",
        "--hidden-import", "csv_processor.gui",
        "--hidden-import", "csv_processor.processor",
        "--hidden-import", "csv_processor.config",
        "--hidden-import", "csv_processor.exceptions",
        "--hidden-import", "csv_processor.ui_components",
        "--hidden-import", "csv_processor.logger",
        "main.py"
    ]
    
    try:
        result = subprocess.run(cmd, check=True)
        
        if (dist_dir / "CSV-Data-Processor").exists():
            print("✓ Linux build successful!")
            print(f"Executable created: {dist_dir / 'CSV-Data-Processor'}")
            return True
        else:
            print("✗ Linux build failed!")
            return False
            
    except subprocess.CalledProcessError:
        print("Linux build failed!")
        return False


def main():
    """Main build function."""
    print("CSV Splitter GUI - Cross-Platform Build Script")
    print("=" * 50)
    
    # Detect platform
    current_platform = detect_platform()
    print(f"Detected platform: {current_platform}")
    
    if current_platform == "unknown":
        print("Unsupported platform for automated builds!")
        print("Try building manually with PyInstaller.")
        sys.exit(1)
    
    # Check and install dependencies
    check_dependencies()
    
    # Change to project root directory
    project_root = Path(__file__).parent.parent
    original_cwd = Path.cwd()
    
    try:
        import os
        os.chdir(project_root)
        
        # Build for current platform
        if current_platform == "windows":
            success = build_windows()
        elif current_platform == "macos":
            success = build_macos()
        elif current_platform == "linux":
            success = build_linux()
        
        if success:
            print("\n✓ Build completed successfully!")
            print(f"Check the 'dist' directory for the executable.")
        else:
            print("\n✗ Build failed!")
            sys.exit(1)
            
    finally:
        os.chdir(original_cwd)


if __name__ == "__main__":
    main()