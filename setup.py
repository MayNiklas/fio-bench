import os

import pkg_resources
from setuptools import find_packages
from setuptools import setup


def read_version(fname="src/fio_bench/version.py"):
    exec(compile(open(fname, encoding="utf-8").read(), fname, "exec"))
    return locals()["__version__"]


setup(
    name="whisper_api",
    version=read_version(),
    url="https://github.com/MayNiklas/fio_bench",
    license="",
    author="MayNiklas",
    author_email="info@niklas-steffen.de",
    description="a simple fio benchmark script",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    readme="README.md",
    python_requires=">=3.7",
    packages=find_packages(where="src", exclude=["tests*"]),
    package_dir={"": "src"},
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ],
    entry_points={
        "console_scripts": [
            "fio_bench=fio_bench.cli:main",
        ],
    },
    extras_require={
        "dev": [
            "pytest",
            "pre-commit",
            "autopep8"
        ]
    },
)
