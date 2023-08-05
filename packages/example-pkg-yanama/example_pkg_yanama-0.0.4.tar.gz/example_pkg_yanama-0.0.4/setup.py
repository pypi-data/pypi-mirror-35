import setuptools

# Get the long description from the README file
with open("README.md", "r") as fh:
    long_description = fh.read()

# Arguments marked as "Required" below must be included for upload to PyPI
# Fields marked as "Optional" may be commented out.

setuptools.setup(
    name="example_pkg_yanama",  # Required
    version="0.0.4",  # Required
    author="Virtustream",  # Optional
    author_email="anjaneyulu.yanamala@emc.com",  # Optional
    description="Testing the setup file to include files",  # Required
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests']),  # Required
    include_package_data=True,  # Optional
    extras_require={  # Optional
        'dev': ['check-manifest'],
        'test': ['coverage'],
    },

)
