import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_pkg_yanama",
    version="0.0.3",
    author="Virtustream",
    author_email="anjaneyulu.yanamala@emc.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    include_package_data=True,


)
