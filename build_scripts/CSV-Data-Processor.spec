# -*- mode: python ; coding: utf-8 -*-

import sys
import os
from pathlib import Path

# Get project paths using PyInstaller's SPECPATH variable
# SPECPATH is automatically set by PyInstaller to the directory containing the spec file
spec_dir = Path(SPECPATH if 'SPECPATH' in globals() else os.path.dirname(os.path.abspath(__file__ if '__file__' in globals() else 'build_scripts')))
project_root = spec_dir.parent  # Go up one level from build_scripts to project root
src_path = project_root / "src"

a = Analysis(
    [str(project_root / 'main.py')],
    pathex=[str(project_root), str(src_path)],
    binaries=[],
    datas=[
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
    cipher=None,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

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
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)