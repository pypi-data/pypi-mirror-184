from setuptools import setup


def long_description():
    with open("README.md") as fp:
        return fp.read()


version = __import__("feather.__init__").__version__
setup(
    name="feather.py",
    author="sarthhh",
    author_email="shiva02939@gmail.com",
    license="MIT",
    url="https://github.com/sarthhh/feather",
    description="SQLITE3 CLI wrapper build on python.",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    version=version,
    python_requires=">=3.8.0",
    include_package_data=True,
    packages=["feather"],
    keywords=["sqlite3", "sqlite", "cli", "database"],
    install_requires=["setuptools", "colorama"],
)
