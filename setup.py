import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="aesthema",
    version="0.1.1",
    description="Modern & visually appealing colormaps for Matplotlib",
    author="jspieler",
    url="https://github.com/jspieler/aesthema",
    license="MIT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["aesthema"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=["cycler", "matplotlib"],
    python_requires=">=3.8",
    extras_require={
        "linting": [
            "pylint",
            "mypy",
        ],
        "testing": ["numpy"],
    },
    include_package_data=True,
)
