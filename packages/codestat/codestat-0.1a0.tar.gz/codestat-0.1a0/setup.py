import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="codestat",
    version="0.1a0",
    author="Fabrizio Destro",
    author_email="destro.fabrizio@gmail.com",
    entry_points={
        'console_scripts': ["codestat=codestat.codestat:main"]
    },
    description="Generate statistics about your code.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ],
    url="https://github.com/dexpota/codestat",
    packages=setuptools.find_packages(),
)
