from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
        name='nagonle-great-module',
        version='0.0.1',
        description='An absolute tragedy',
        py_modules=["great_module"],
        package_dir={'': 'src'},
        long_description=long_description,
        long_description_content_type="text/markdown",
        extras_require = {
            "dev": [
                "pytest>=7.1",
                "twine>=4.0",
            ],
        },
        url="https://github.com/nagonle/great_module",
        author="Nicolas Gonzalez",
        author_email="nicolas.gonzalez.cl@gmail.com",
)
