import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# with open('requirements.txt', 'r') as fin:
#     reqs = fin.read().splitlines()
# print(f"requirements: {reqs}")

# This call to setup() does all the work
setup(
    name="fieldday",
    version="0.0.1",
    description="Data field manager for IoT applications",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jmfife/fieldday",
    author="Mike Fife",
    author_email="jmfife@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["fieldday"],
    include_package_data=True,
    entry_points={
    },
    install_requires=[],
    python_requires='>=3.7',
    extras_require={
        "qty": ["pint"],
    }
)