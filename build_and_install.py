#!/usr/bin/env python3
"""
Build and install script for qvest package
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"🔧 {description}...")
    try:
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        if result.stdout:
            print(f"   Output: {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed:")
        print(f"   Error: {e.stderr.strip()}")
        return False

def clean_build():
    """Clean previous build artifacts"""
    print("🧹 Cleaning previous build artifacts...")
    
    dirs_to_clean = ["build", "dist", "qvest.egg-info"]
    for dir_name in dirs_to_clean:
        dir_path = Path(dir_name)
        if dir_path.exists():
            if os.name == 'nt':  # Windows
                run_command(f'rmdir /s /q "{dir_path}"', f"Removing {dir_name}")
            else:  # Unix/Linux/Mac
                run_command(f'rm -rf "{dir_path}"', f"Removing {dir_name}")
    
    print("✅ Cleanup completed")

def build_package():
    """Build the package"""
    steps = [
        ("python -m pip install --upgrade build", "Installing/upgrading build tools"),
        ("python -m build", "Building package"),
    ]
    
    for cmd, description in steps:
        if not run_command(cmd, description):
            return False
    
    return True

def install_package():
    """Install the package locally"""
    print("📦 Installing qvest locally...")
    
    # First uninstall if already installed
    subprocess.run("pip uninstall -y qvest", shell=True, capture_output=True)
    
    # Install from built wheel
    dist_files = list(Path("dist").glob("*.whl"))
    if not dist_files:
        print("❌ No wheel file found in dist/")
        return False
    
    wheel_file = dist_files[0]
    return run_command(f'pip install "{wheel_file}"', "Installing qvest package")

def test_installation():
    """Test the installed package"""
    print("🧪 Testing installed package...")
    
    test_commands = [
        ("qvest --version", "Testing CLI version command"),
        ("qvest --help", "Testing CLI help command"),
        ("python -c 'import qvest; print(f\"qvest {qvest.__version__} imported successfully\")'", "Testing package import")
    ]
    
    for cmd, description in test_commands:
        if not run_command(cmd, description):
            return False
    
    return True

def main():
    """Main build and install process"""
    print("🚀 Q VEST Build & Install Script")
    print("=" * 40)
    
    if not Path("setup.py").exists():
        print("❌ setup.py not found. Run this script from the package root directory.")
        sys.exit(1)
    
    steps = [
        ("Clean build artifacts", clean_build),
        ("Build package", build_package), 
        ("Install package", install_package),
        ("Test installation", test_installation)
    ]
    
    for step_name, step_func in steps:
        print(f"\n📋 Step: {step_name}")
        print("-" * 30)
        if not step_func():
            print(f"❌ Failed at step: {step_name}")
            sys.exit(1)
    
    print("\n🎉 Build and installation completed successfully!")
    print("\nYou can now run:")
    print("  qvest                    # Run portfolio optimization")
    print("  qvest config             # Configure API key")
    print("  qvest --help             # Show help")
    
    print("\nTo publish to PyPI:")
    print("  python -m twine upload dist/*")

if __name__ == "__main__":
    main()
