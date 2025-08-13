# QVEST CLI Installation & Usage Guide

## 📋 Complete Step-by-Step Guide

This document provides all the commands and steps to build, install, and use the QVEST CLI - your IBM Quantum-powered portfolio optimization tool.

---

## 🎯 Table of Contents

1. [Prerequisites](#prerequisites)
2. [Building the Package](#building-the-package)
3. [Installing QVEST](#installing-qvest)
4. [Using QVEST](#using-qvest)
5. [Configuration Management](#configuration-management)
6. [Publishing to PyPI](#publishing-to-pypi)
7. [Troubleshooting](#troubleshooting)

---

## 📋 Prerequisites

### System Requirements
- **Python 3.8+** installed
- **PowerShell** (Windows) or **Terminal** (macOS/Linux)
- Internet connection for package downloads and market data

### IBM Quantum Account
1. Visit: https://quantum-computing.ibm.com/
2. Create a free account or sign in
3. Go to **Account Settings** → **API Token**
4. Copy your API Token (you'll need this later)

---

## 🔧 Building the Package

### Step 1: Install Build Tools
```bash
pip install --upgrade build wheel twine
```

### Step 2: Clean Previous Builds (if any)
```bash
# Windows PowerShell
Remove-Item -Recurse -Force -ErrorAction SilentlyContinue build, dist, qvest.egg-info

# macOS/Linux
rm -rf build dist qvest.egg-info
```

### Step 3: Build the Package
```bash
python -m build
```

**Expected Output:**
- Creates `dist/qvest-1.0.0-py3-none-any.whl` (wheel file)
- Creates `dist/qvest-1.0.0.tar.gz` (source distribution)

### Step 4: Verify Build Files
```bash
# Windows PowerShell
Get-ChildItem dist

# macOS/Linux
ls -la dist/
```

**Expected Files:**
```
qvest-1.0.0-py3-none-any.whl
qvest-1.0.0.tar.gz
```

---

## 📦 Installing QVEST

### Option 1: Install from Local Build (Recommended for Development)
```bash
# Uninstall any existing version
pip uninstall -y qvest

# Install from local wheel
pip install dist/qvest-1.0.0-py3-none-any.whl
```

### Option 2: Install from PyPI (Once Published)
```bash
pip install qvest
```

### Verify Installation
```bash
qvest --version
```
**Expected Output:** `qvest 1.0.0`

```bash
qvest --help
```
**Expected Output:** Full help documentation

---

## 🚀 Using QVEST

### First-Time Setup
When you run QVEST for the first time, it will guide you through API key setup:

```bash
qvest
```

**What happens:**
1. Shows welcome message and QVEST banner
2. Prompts for IBM Quantum API key
3. Optionally asks for IBM Quantum instance (for IBM Cloud users)
4. Saves credentials securely to `~/.qvest/config.json`
5. Launches portfolio optimization

### Interactive Portfolio Optimization

The CLI will guide you through:

1. **Market Sector Selection:**
   ```
   Please select a market sector:
   1. Tech
   2. Healthcare  
   3. Finance
   4. Energy
   5. Custom
   Enter your choice (1-5):
   ```

2. **Risk Level:**
   ```
   Enter risk level (1-10): 7
   ```

3. **Investment Amount:**
   ```
   Enter investment amount (USD): 10000
   ```

4. **Time Horizon:**
   ```
   Enter prediction horizon (years): 5
   ```

5. **Algorithm Mode:**
   ```
   Select execution mode:
   1. Normal (Quantum + classical refinement)
   2. Pure Quantum (bitstring allocation only)
   Enter your choice (1-2) [2]:
   ```

### Expected Output Example
```
✅ Prediction result:
==================================================
🧮 Algorithm: Pure Quantum QAOA
💰 Expected Return: 12.34%
📊 Portfolio Allocation:
   • AAPL: 35.2%
   • MSFT: 28.7%
   • NVDA: 21.1%
   • GOOGL: 15.0%
⚡ Quantum Advantage: 2.3x speedup
==================================================

🎉 Portfolio optimization completed successfully!
```

---

## ⚙️ Configuration Management

### Check Configuration Status
```bash
qvest config --status
```
**Output:**
```
📋 Configuration Status
Config file: C:\Users\YourName\.qvest\config.json
Exists: ✅
API Key: ✅ abc12345...xyz9
Instance: Not set (using Platform)
```

### Setup or Update API Key
```bash
qvest config
```
**Interactive setup for first-time users**

```bash
qvest config --update
```
**Update existing configuration**

### Clear Configuration
```bash
qvest config --clear
```
**Removes all stored credentials**

### Configuration File Location
- **Windows:** `C:\Users\YourName\.qvest\config.json`
- **macOS/Linux:** `~/.qvest/config.json`

### Configuration File Format
```json
{
  "ibm_quantum_token": "your_api_token_here",
  "ibm_quantum_instance": "hub/group/project"
}
```

---

## 📤 Publishing to PyPI

### Step 1: Create PyPI Account
1. Visit: https://pypi.org/
2. Create account and verify email
3. Generate API token in account settings

### Step 2: Test on Test PyPI (Optional)
```bash
# Upload to test PyPI
python -m twine upload --repository testpypi dist/*

# Test installation from test PyPI
pip install --index-url https://test.pypi.org/simple/ qvest
```

### Step 3: Publish to Real PyPI
```bash
python -m twine upload dist/*
```

### Step 4: Verify Publication
```bash
pip install qvest
qvest --version
```

---

## 🐛 Troubleshooting

### Common Issues & Solutions

#### 1. "qvest: command not found"
**Solution:**
```bash
# Reinstall the package
pip uninstall -y qvest
pip install dist/qvest-1.0.0-py3-none-any.whl

# Verify Python scripts directory is in PATH
python -m site --user-site
```

#### 2. Build Failures
**Solution:**
```bash
# Install/upgrade build tools
pip install --upgrade build setuptools wheel

# Clean and rebuild
Remove-Item -Recurse -Force build, dist, qvest.egg-info  # Windows
python -m build
```

#### 3. Import Errors
**Solution:**
```bash
# Test package structure
python test_package.py

# Verify dependencies
pip install numpy pandas yfinance scipy qiskit qiskit-ibm-runtime qiskit-aer python-dotenv
```

#### 4. API Key Issues
**Solution:**
```bash
# Check configuration
qvest config --status

# Reset configuration
qvest config --clear
qvest config

# Verify API key at: https://quantum-computing.ibm.com/account
```

#### 5. Quantum Connection Problems
**Common Solutions:**
- Verify IBM Quantum API key is valid
- Check internet connection
- Try running with local simulator fallback
- Update qiskit packages: `pip install --upgrade qiskit qiskit-ibm-runtime`

---

## 🎛️ Advanced Usage

### Using Different Python Environments
```bash
# Create virtual environment
python -m venv qvest-env

# Windows
qvest-env\Scripts\activate

# macOS/Linux  
source qvest-env/bin/activate

# Install QVEST
pip install dist/qvest-1.0.0-py3-none-any.whl
```

### Running QVEST as Python Module
```bash
# Alternative way to run QVEST
python -m qvest

# With specific configuration
python -m qvest config --status
```

### Batch/Automated Usage
For automated setups, you can pre-configure the API key:

```python
import json
from pathlib import Path

# Create config directory and file
config_dir = Path.home() / ".qvest"
config_dir.mkdir(exist_ok=True)

config = {
    "ibm_quantum_token": "your_api_token_here",
    "ibm_quantum_instance": "optional_instance"
}

with open(config_dir / "config.json", "w") as f:
    json.dump(config, f, indent=2)
```

---

## 📊 Development Commands Summary

### Complete Build & Test Workflow
```bash
# 1. Test package structure
python test_package.py

# 2. Clean previous builds
Remove-Item -Recurse -Force build, dist, qvest.egg-info

# 3. Build package
python -m build

# 4. Install locally
pip uninstall -y qvest
pip install dist/qvest-1.0.0-py3-none-any.whl

# 5. Test installation
qvest --version
qvest config --status
qvest --help

# 6. Optional: Run full test
qvest  # Interactive test
```

### All QVEST CLI Commands
```bash
# Main commands
qvest                     # Run portfolio optimization
qvest --version          # Show version
qvest --help            # Show help

# Configuration commands
qvest config            # Setup API key
qvest config --status   # Show config status  
qvest config --update   # Update configuration
qvest config --clear    # Clear configuration
qvest config --help     # Show config help
```

---

## 🎉 Success Verification Checklist

- [ ] Package builds successfully (`python -m build`)
- [ ] Package installs without errors (`pip install dist/qvest-*.whl`)
- [ ] CLI command works (`qvest --version`)
- [ ] Help system works (`qvest --help`)
- [ ] Config management works (`qvest config --status`)
- [ ] Package imports correctly (`python -c "import qvest"`)
- [ ] Full workflow runs (`qvest` interactive test)

---

## 📞 Support & Resources

- **IBM Quantum Platform:** https://quantum-computing.ibm.com/
- **Python Packaging Guide:** https://packaging.python.org/
- **PyPI:** https://pypi.org/
- **Qiskit Documentation:** https://qiskit.org/documentation/

---

**Made with ⚡ by Minhal Rizvi**

*This guide covers all the steps to transform your prediction.py into a professional, PyPI-ready CLI tool that users can install globally and use with a simple `qvest` command.*
