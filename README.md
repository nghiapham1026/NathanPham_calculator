python -m tests.test_calculator
python -m tests.unittest_calculator
python -m tests.test_advanced_operations
python -m tests.test_basic_operations
python -m tests.test_complex_numbers
python -m tests.test_logarithms
python -m tests.test_statistics
python -m tests.test_trigonometry


python setup.py sdist bdist_wheel
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ NathanPham_calculator
