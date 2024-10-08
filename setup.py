import setuptools

setuptools.setup(
    name="NathanPham_calculator",  # Change to your preferred package name
    version="0.1.0",
    author="Nathan Pham",  # Replace with your name
    author_email="nghia.pham@sjsu.edu",  # Replace with your email
    description="An advanced calculator package",  # Brief description of your package
    long_description=open('README.md').read(),  # Long description read from README file
    long_description_content_type="text/markdown",
    url="https://github.com/nghiapham1026/NathanPham_calculator",  # URL to your package repository
    packages=setuptools.find_packages(),  # Automatically find packages in your project
    classifiers=[
        "Programming Language :: Python :: 3",  # Specify supported Python versions
        "License :: OSI Approved :: MIT License",  # License type (adjust if needed)
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version required
)
