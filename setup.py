from setuptools import setup, find_packages

setup(
    name='nathan_calculator',  # Name of your package
    version='0.1',  # Initial version
    author='Nathan Pham',  # Your name
    author_email='nathan@example.com',  # Your email
    description='A simple Python calculator for basic and advanced operations',
    long_description=open('README.md').read(),  # Make sure you have a README.md file
    long_description_content_type='text/markdown',  # If your README is in markdown format
    url='https://github.com/nghiapham1026/nathan_calculator',  # URL to your repository (if any)
    packages=find_packages(),  # Automatically finds all packages in the directory
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Choose your license, e.g., MIT, Apache, etc.
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Minimum Python version requirement
    install_requires=[
        # List any third-party dependencies your project needs
    ],
)
