#!/usr/bin/env python3
"""
Project validation for Prescription Finder.
Kivy GUI apps cannot run in Replit's web environment - this validates the project structure.
"""
import sys
import py_compile
import os

print("=" * 60)
print("PRESCRIPTION FINDER - APK BUILD PREPARATION")
print("=" * 60)
print()

# Check syntax
try:
    py_compile.compile('main.py', doraise=True)
    print("✓ main.py syntax is valid")
except py_compile.PyCompileError as e:
    print(f"✗ Syntax error: {e}")
    sys.exit(1)

# Check required files
files = ['main.py', 'buildozer.spec', 'requirements.txt', 'build_instructions.txt']
for f in files:
    if os.path.exists(f):
        print(f"✓ {f} exists")
    else:
        print(f"✗ {f} missing")
        sys.exit(1)

print()
print("=" * 60)
print("✓ PROJECT IS READY FOR APK BUILD")
print()
print("NOTE: Kivy GUI apps cannot display in Replit's web environment.")
print("To build the Android APK, follow these steps:")
print()
print("1. Download this project to your local Linux machine")
print("2. Open build_instructions.txt for detailed instructions")
print("3. Run: buildozer android debug")
print("=" * 60)
