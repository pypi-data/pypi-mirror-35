import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lipsumAPI",
    version="1.0",
    author="Theo Toth",
    author_email="lipsumapi@xed.re",
    description="A lipsum.com API for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/xedre/Python-Lipsum-API",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Internet",
        "Topic :: Utilities",
    ],
)
