# Q VEST Setup Guide

This guide will help you build, install, and distribute the qvest package.

## 📋 Package Structure

Your PyPI-ready package now has this structure:

```
qvest/
├── qvest/                      # Main package directory
│   ├── __init__.py            # Package initialization
│   ├── __main__.py            # CLI entry point
│   ├── config_manager.py      # API key management
│   └── prediction.py          # Quantum optimization engine
├── setup.py                   # Package setup (legacy)
├── pyproject.toml            # Modern build configuration
├── README.md                 # Documentation
├── LICENSE                   # MIT License
├── MANIFEST.in              # Package data inclusion
├── build_and_install.py     # Build automation script
├── test_package.py          # Package testing script
└── SETUP_GUIDE.md          # This file
```

## 🚀 Quick Start

### 1. Test Package Structure
```bash
python test_package.py
```

### 2. Build and Install Locally
```bash
python build_and_install.py
```

### 3. Test CLI
```bash
qvest --version
qvest --help
```

## 🔧 Manual Setup Steps

If you prefer manual control:

### 1. Install Build Tools
```bash
pip install --upgrade build twine
```

### 2. Clean Previous Builds
```bash
# Windows
rmdir /s /q build dist qvest.egg-info

# Unix/Linux/macOS
rm -rf build dist qvest.egg-info
```

### 3. Build Package
```bash
python -m build
```

This creates:
- `dist/qvest-1.0.0.tar.gz` (source distribution)
- `dist/qvest-1.0.0-py3-none-any.whl` (wheel)

### 4. Install Locally
```bash
pip install dist/qvest-1.0.0-py3-none-any.whl
```

### 5. Test Installation
```bash
qvest --version
qvest config --status
```

## 📦 Publishing to PyPI

### 1. Test on PyPI Test Server
```bash
# Upload to test PyPI
python -m twine upload --repository testpypi dist/*

# Install from test PyPI
pip install --index-url https://test.pypi.org/simple/ qvest
```

### 2. Publish to Real PyPI
```bash
python -m twine upload dist/*
```

### 3. Install from PyPI
```bash
pip install qvest
```

## 🎯 Usage Examples

### First Time Setup
```bash
# Install from PyPI
pip install qvest

# Run qvest (will prompt for API key)
qvest
```

### Configuration Management
```bash
# Show current config
qvest config --status

# Update configuration
qvest config --update

# Clear all config
qvest config --clear
```

### Portfolio Optimization
```bash
# Run with existing config
qvest

# The CLI will guide you through:
# 1. Market sector selection
# 2. Risk level (1-10)
# 3. Investment amount
# 4. Time horizon
# 5. Algorithm mode
```

## 🔑 API Key Setup

Users need an IBM Quantum API key:

1. Visit: https://quantum-computing.ibm.com/
2. Create free account
3. Go to Account Settings
4. Copy API Token
5. Run `qvest` or `qvest config` to set it up

The key is stored securely in `~/.qvest/config.json`.

## 🛠 Development

### Adding Features

1. **New CLI Commands**: Edit `qvest/__main__.py`
2. **Configuration Options**: Edit `qvest/config_manager.py`
3. **Quantum Algorithms**: Edit `qvest/prediction.py`
4. **Package Info**: Update `qvest/__init__.py` and `setup.py`

### Testing Changes

```bash
# Test package structure
python test_package.py

# Build and install locally
python build_and_install.py

# Test manually
qvest --help
```

### Version Updates

1. Update version in:
   - `setup.py`
   - `pyproject.toml`
   - `qvest/__init__.py`
   - `qvest/__main__.py`

2. Rebuild and republish

## 🐛 Troubleshooting

### Build Issues
- Ensure Python 3.8+ is installed
- Install build tools: `pip install build wheel`
- Check for syntax errors in Python files

### Import Errors
- Verify package structure with `test_package.py`
- Check `__init__.py` files exist
- Ensure dependencies are listed in `setup.py`

### CLI Not Working
- Reinstall: `pip uninstall qvest && pip install qvest`
- Check entry point in `setup.py`
- Test with `python -m qvest`

### API Key Issues
- Run `qvest config --status` to check configuration
- Clear and reconfigure: `qvest config --clear`
- Verify API key at https://quantum-computing.ibm.com/

## 📄 File Descriptions

- **`setup.py`**: Legacy package configuration for pip
- **`pyproject.toml`**: Modern Python packaging standard
- **`qvest/__main__.py`**: CLI entry point with argument parsing
- **`qvest/config_manager.py`**: Secure API key storage and management
- **`qvest/prediction.py`**: Core quantum optimization engine
- **`README.md`**: User documentation and installation guide
- **`LICENSE`**: MIT license for open source distribution
- **`MANIFEST.in`**: Controls which files are included in distribution

## 🎉 Success!

After following this guide, users can:

```bash
pip install qvest
qvest
```

And get a fully functional quantum portfolio optimization CLI!

---

**Next Steps:**
1. Test the package thoroughly
2. Create a GitHub repository
3. Set up CI/CD for automated testing
4. Publish to PyPI
5. Share with the quantum computing community!
