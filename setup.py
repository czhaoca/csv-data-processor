#!/usr/bin/env python3
"""
Setup script for CSV Splitter GUI application.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
readme_path = Path(__file__).parent / "docs" / "README.md"
if readme_path.exists():
    with open(readme_path, "r", encoding="utf-8") as f:
        long_description = f.read()
else:
    long_description = "A modern, modular Python GUI application for splitting CSV files."

# Read requirements
requirements_path = Path(__file__).parent / "requirements.txt"
if requirements_path.exists():
    with open(requirements_path, "r", encoding="utf-8") as f:
        requirements = [
            line.strip() 
            for line in f 
            if line.strip() and not line.startswith("#") and not line.startswith("-")
        ]
else:
    requirements = []

# Filter out development dependencies for production install
install_requires = []
extras_require = {
    "dev": [],
    "test": []
}

for req in requirements:
    if any(keyword in req.lower() for keyword in ["pytest", "black", "flake8", "mypy", "isort", "sphinx"]):
        if "pytest" in req.lower():
            extras_require["test"].append(req)
        else:
            extras_require["dev"].append(req)
    else:
        install_requires.append(req)

setup(
    name="csv-splitter-gui",
    version="2.0.0",
    author="CSV Splitter Team",
    author_email="",
    description="A modern, modular Python GUI application for splitting CSV files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/csv-splitter-gui",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Developers",
        "Topic :: Office/Business",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: X11 Applications :: Qt",
        "Environment :: MacOS X",
        "Environment :: Win32 (MS Windows)",
    ],
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require=extras_require,
    entry_points={
        "console_scripts": [
            "csv-splitter=csv_splitter.cli:main",
        ],
        "gui_scripts": [
            "csv-splitter-gui=main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "csv_splitter": ["*.py"],
    },
    keywords="csv, data, processing, gui, tkinter, file-management",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/csv-splitter-gui/issues",
        "Source": "https://github.com/yourusername/csv-splitter-gui",
        "Documentation": "https://github.com/yourusername/csv-splitter-gui/tree/main/docs",
    },
)