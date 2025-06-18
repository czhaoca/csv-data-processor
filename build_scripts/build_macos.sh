#!/bin/bash
# Build script for macOS application bundle using PyInstaller

echo "Building CSV Splitter GUI for macOS..."

# Check if PyInstaller is installed
if ! python3 -c "import PyInstaller" 2>/dev/null; then
    echo "PyInstaller not found. Installing..."
    pip3 install pyinstaller
fi

# Clean previous builds
rm -rf dist build

# Create the application bundle
echo "Creating macOS application bundle..."
pyinstaller --clean \
    --onefile \
    --windowed \
    --name "CSV-Splitter-GUI" \
    --add-data "src/csv_splitter:csv_splitter" \
    --hidden-import "csv_splitter" \
    --hidden-import "csv_splitter.gui" \
    --hidden-import "csv_splitter.processor" \
    --hidden-import "csv_splitter.config" \
    --hidden-import "csv_splitter.exceptions" \
    --hidden-import "csv_splitter.ui_components" \
    --hidden-import "csv_splitter.logger" \
    main.py

if [ -f "dist/CSV-Splitter-GUI" ]; then
    echo ""
    echo "✓ Build successful!"
    echo "Application created: dist/CSV-Splitter-GUI"
    echo "File size: $(ls -lh dist/CSV-Splitter-GUI | awk '{print $5}')"
    
    # Make it executable
    chmod +x dist/CSV-Splitter-GUI
    
    # Create a simple .app bundle structure for better macOS integration
    echo "Creating .app bundle..."
    mkdir -p "dist/CSV Splitter GUI.app/Contents/MacOS"
    mkdir -p "dist/CSV Splitter GUI.app/Contents/Resources"
    
    # Move executable to app bundle
    mv "dist/CSV-Splitter-GUI" "dist/CSV Splitter GUI.app/Contents/MacOS/"
    
    # Create Info.plist
    cat > "dist/CSV Splitter GUI.app/Contents/Info.plist" << EOF
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleExecutable</key>
    <string>CSV-Splitter-GUI</string>
    <key>CFBundleIdentifier</key>
    <string>com.csvspiltter.gui</string>
    <key>CFBundleName</key>
    <string>CSV Splitter GUI</string>
    <key>CFBundleDisplayName</key>
    <string>CSV Splitter GUI</string>
    <key>CFBundleVersion</key>
    <string>2.0.0</string>
    <key>CFBundleShortVersionString</key>
    <string>2.0.0</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>LSMinimumSystemVersion</key>
    <string>10.10</string>
    <key>LSApplicationCategoryType</key>
    <string>public.app-category.productivity</string>
    <key>NSHighResolutionCapable</key>
    <true/>
</dict>
</plist>
EOF
    
    echo "✓ macOS .app bundle created: dist/CSV Splitter GUI.app"
else
    echo ""
    echo "✗ Build failed!"
    exit 1
fi

echo ""
echo "To distribute:"
echo "1. Test the application: open 'dist/CSV Splitter GUI.app'"
echo "2. Create DMG: hdiutil create -volname 'CSV Splitter GUI' -srcfolder 'dist/CSV Splitter GUI.app' -ov -format UDZO 'CSV-Splitter-GUI-macOS.dmg'"
echo "3. The .app bundle is self-contained and includes all dependencies"
echo "4. Users can drag it to Applications folder"