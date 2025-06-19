#!/usr/bin/env python3
"""
PyInstaller spec file for building CSV Data Processor executables.
"""

import sys
from pathlib import Path

# Get the project root directory
project_root = Path(__file__).parent.parent
src_path = project_root / "src"
main_script = project_root / "main.py"

# Add src to Python path for imports
sys.path.insert(0, str(src_path))

block_cipher = None

a = Analysis(
    [str(main_script)],
    pathex=[str(project_root), str(src_path)],
    binaries=[],
    datas=[
        # Include source package
        (str(src_path / "csv_processor"), "csv_processor"),
    ],
    hiddenimports=[
        'csv_processor',
        'csv_processor.gui',
        'csv_processor.processor',
        'csv_processor.config',
        'csv_processor.exceptions',
        'csv_processor.ui_components',
        'csv_processor.logger',
        'tkinter',
        'tkinter.ttk',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'tkinter.font',
        'tkinter.scrolledtext',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CSV-Data-Processor',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to False for GUI app (no console window)
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # Add icon file path here if you have one
)