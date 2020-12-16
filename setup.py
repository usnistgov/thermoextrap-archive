from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="cmomy",
    version="0.0.2",
    description="Central (co)moment calculation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
    keywords="data analysis",
    url="https://github.com/wpk-nist-gov/cmomy",
    author="William Krekelberg",
    author_email="wpk@nist.gov",
    license="NIST license https://www.nist.gov/director/licensing",
    # packages=['cmomy'],
    packages=find_packages(), 
    install_requires=["numpy", "numba", "xarray"],
    # testing
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    test_suite="pytest",
    include_package_data=True,
    zip_safe=True,
)
