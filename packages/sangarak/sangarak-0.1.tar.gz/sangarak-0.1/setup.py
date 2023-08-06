from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='sangarak',
    version='0.1',
    description='Python library for reading matrices from many files and generating a single numpy matrix',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='BSD 3-clause',
    packages=find_packages(),
    author='Sameer Deshmukh',
    author_email='sameer.desmukh93@gmail.com',
    keywords=['numpy', 'mpi', 'matrix'],
    install_requires=[
        'numpy',
    ],
    url='https://github.com/rioyokotalab/sangarak',
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent"
    ]
)
