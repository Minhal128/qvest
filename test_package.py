#!/usr/bin/env python3
"""
Test script to verify qvest package structure and basic functionality
"""

import sys
import importlib.util
from pathlib import Path

def test_imports():
    """Test if all modules can be imported"""
    print("🧪 Testing package imports...")
    
    try:
        # Test basic imports
        from qvest.config_manager import ConfigManager
        from qvest.prediction import QuantumPortfolioOptimizer
        from qvest import __version__, __author__
        
        print(f"✅ Package version: {__version__}")
        print(f"✅ Package author: {__author__}")
        print("✅ All modules imported successfully")
        
        # Test ConfigManager initialization
        config = ConfigManager()
        print(f"✅ ConfigManager initialized: {config.config_file}")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False

def test_package_structure():
    """Test package structure"""
    print("\n📁 Testing package structure...")
    
    required_files = [
        "setup.py",
        "pyproject.toml", 
        "README.md",
        "LICENSE",
        "MANIFEST.in",
        "qvest/__init__.py",
        "qvest/__main__.py",
        "qvest/config_manager.py",
        "qvest/prediction.py"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print(f"❌ Missing files: {missing_files}")
        return False
    else:
        print("✅ All required files present")
        return True

def test_cli_entry_point():
    """Test CLI entry point"""
    print("\n⚙️ Testing CLI entry point...")
    
    try:
        from qvest.__main__ import main
        print("✅ CLI entry point accessible")
        return True
    except ImportError as e:
        print(f"❌ CLI entry point error: {e}")
        return False

def main():
    """Run all tests"""
    print("🚀 Q VEST Package Test Suite")
    print("=" * 40)
    
    tests = [
        test_package_structure,
        test_imports,
        test_cli_entry_point
    ]
    
    passed = 0
    for test in tests:
        if test():
            passed += 1
    
    print(f"\n📊 Test Results: {passed}/{len(tests)} tests passed")
    
    if passed == len(tests):
        print("🎉 All tests passed! Package is ready for distribution.")
    else:
        print("❌ Some tests failed. Please fix issues before publishing.")
        sys.exit(1)

if __name__ == "__main__":
    main()
