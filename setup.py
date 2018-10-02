from setuptools import setup, find_packages

setup(
    name='pycalc',
    version='1.0',
    author='Yury Kliachko',
    author_email='yury_kliachko@epam.com',
    packages=find_packages(),
    entry_points={'console_scripts': ['pycalc = pycalc.__main__:main']},
    test_suit='tests'
)