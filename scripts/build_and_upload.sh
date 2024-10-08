#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Function to display usage information
usage() {
    echo "Usage: $0 [test|prod]"
    echo "  test: Upload to TestPyPI and install from TestPyPI"
    echo "  prod: Upload to PyPI and install from PyPI"
    exit 1
}

# Upgrade pip and install required packages
echo "Upgrading pip and installing required packages..."
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade setuptools wheel twine

# Clean previous builds
echo "Cleaning up previous builds..."
rm -rf build/ dist/ NathanPham_calculator.egg-info/

# Run unit tests
echo "Running unit tests..."
python3 -m unittest discover tests

# Build the package
echo "Building the package..."
python3 setup.py sdist bdist_wheel

# Check the distribution files
echo "Checking the distribution files..."
twine check dist/*

# Upload the package
if [ "$1" == "test" ]; then
    echo "Uploading the package to TestPyPI..."
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
else
    echo "Uploading the package to PyPI..."
    twine upload dist/*
fi

# Install the package
echo "Installing the package..."
python3 -m pip install --index-url https://test.pypi.org/simple/ NathanPham_calculator --no-deps

# Deactivate virtual environment if necessary
deactivate

echo "Done!"
