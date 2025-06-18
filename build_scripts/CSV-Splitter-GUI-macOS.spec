# -*- mode: python ; coding: utf-8 -*-

import sys
from pathlib import Path

# Get project paths
project_root = Path.cwd()
src_path = project_root / "src"

a = Analysis(
    ['main.py'],
    pathex=[str(project_root), str(src_path)],
    binaries=[],
    datas=[
        (str(src_path / "csv_splitter"), "csv_splitter"),
    ],
    hiddenimports=[
        'csv_splitter',
        'csv_splitter.gui',
        'csv_splitter.processor',
        'csv_splitter.config',
        'csv_splitter.exceptions',
        'csv_splitter.ui_components',
        'csv_splitter.logger',
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
    [],
    exclude_binaries=True,
    name='CSV-Splitter-GUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='CSV-Splitter-GUI',
)

app = BUNDLE(
    coll,
    name='CSV-Splitter-GUI.app',
    icon=None,
    bundle_identifier='com.csvspitter.gui',
)