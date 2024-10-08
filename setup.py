import setuptools

setuptools.setup(
    name="NathanPham_calculator",
    version="0.1.1",
    author="Nathan Pham",
    author_email="nghia.pham@sjsu.edu",
    description="An advanced calculator package",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/nghiapham1026/NathanPham_calculator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)