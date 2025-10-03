# Prescription Finder

## Overview

Prescription Finder is a mobile application built with Kivy and KivyMD that helps users find appropriate medication recommendations based on age, weight, and symptoms. The application matches user inputs against a predefined prescription database stored in JSON format and displays relevant medication information including dosage instructions.

The application is designed to be built as an Android APK and provides a simple, user-friendly interface for querying medical prescriptions based on patient demographics and symptoms.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Framework Choice: Kivy + KivyMD**
- **Decision**: Uses Kivy as the core UI framework with KivyMD for Material Design components
- **Rationale**: Kivy enables cross-platform mobile development with Python, while KivyMD provides modern Material Design UI elements
- **Approach**: KV language for declarative UI definition separated from application logic
- **UI Components**: 
  - Material Design Cards for containing form elements
  - Text fields with validation (age as integer, weight as float, symptoms as text)
  - Raised button for form submission
  - Results display area (implementation incomplete in current codebase)

### Data Layer

**Local JSON Storage**
- **Decision**: Static JSON file (`Priscription.json`) for prescription data storage
- **Structure**: Nested object containing array of prescription records with fields:
  - Age range (age_min, age_max)
  - Weight range (weight_min, weight_max)
  - Symptom identifier
  - Medicine name
  - Dosage instructions
- **Storage Access**: Kivy's JsonStore for reading prescription data
- **Trade-offs**: 
  - **Pros**: Simple, no server required, fast local access, works offline
  - **Cons**: Limited scalability, requires app update to modify prescription data, no user-specific data persistence

### Application Logic

**Prescription Matching Algorithm**
- **Decision**: Range-based filtering system
- **Approach**: Matches user input against prescription records where:
  - User age falls within age_min and age_max
  - User weight falls within weight_min and weight_max
  - User symptom matches symptom field (likely case-insensitive)
- **Alternative Considered**: Rule-based expert system or weighted scoring
- **Chosen Approach Benefits**: Simple, deterministic, easy to understand and debug

### Build and Deployment

**Android APK Compilation**
- **Tool**: Buildozer for packaging Python/Kivy apps as Android APKs
- **Requirements**: Linux environment (native, GitHub Actions, or Google Colab)
- **Build Configuration**: buildozer.spec file configured for Android API 33, supports arm64-v8a and armeabi-v7a architectures
- **Current Status**: Project is ready for APK build with all configuration files in place
- **Deployment Options**:
  1. Local Linux build (30-60 minutes first build)
  2. GitHub Actions CI/CD automation
  3. Google Colab cloud building

## External Dependencies

### Core Frameworks
- **Kivy (v2.3.0)**: Cross-platform Python framework for multi-touch applications
- **KivyMD (v1.2.0)**: Material Design component library for Kivy

### Build Tools
- **Buildozer**: Python-to-Android APK compilation tool
- **Cython**: Required for Buildozer compilation process
- **Java Development Kit (JDK 17)**: Required for Android build process

### System Dependencies (Linux Build Environment)
- Git, zip, unzip utilities
- OpenJDK 17
- Build tools: autoconf, libtool, pkg-config, cmake
- Development libraries: zlib, ncurses, libffi, OpenSSL

### Data Storage
- **Kivy JsonStore**: Built-in JSON storage mechanism for local data persistence
- **No external database**: All data stored in flat JSON files within the application bundle

## Recent Changes

**October 3, 2025**: APK Build Preparation Complete
- Created buildozer.spec configuration file with Android build settings
- Created requirements.txt with Kivy 2.3.0 and KivyMD 1.2.0 dependencies
- Created build_instructions.txt with detailed steps for building APK on Linux, GitHub Actions, or Google Colab
- Created GitHub Actions workflow (.github/workflows/build-apk.yml) for automated APK builds
- Created GITHUB_BUILD_GUIDE.txt with step-by-step instructions for GitHub Actions setup
- Application is fully implemented with complete UI and prescription matching logic
- Project structure optimized for Buildozer compilation

## Project Files

- **main.py**: Complete Kivy/KivyMD application with Material Design UI
- **buildozer.spec**: Android build configuration (API 33, multi-arch support)
- **requirements.txt**: Python package dependencies
- **build_instructions.txt**: Step-by-step APK build guide (manual builds)
- **GITHUB_BUILD_GUIDE.txt**: Complete guide for GitHub Actions automated builds
- **.github/workflows/build-apk.yml**: GitHub Actions workflow for automated APK compilation
- **.gitignore**: Excludes build artifacts and cache files
- **validate_project.py**: Validation script (verifies project structure and syntax)

## Important Notes

- This is a Kivy GUI application designed for mobile devices
- The GUI cannot run in Replit's web-based environment (requires display)
- To build the APK, download the project and follow build_instructions.txt on a Linux system
- First APK build typically takes 30-60 minutes (downloads Android SDK/NDK)