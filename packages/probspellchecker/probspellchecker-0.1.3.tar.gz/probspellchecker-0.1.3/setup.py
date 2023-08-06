from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="probspellchecker",
    version="0.1.3",
    description="probabilistic spell checker",
    license="LGPLv3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="digitalarbeiter",
    author_email="digitalarbeiter@talbriefkasten.de",
    url="https://github.com/digitalarbeiter/probspellchecker",
    packages=["probspellchecker"],
    install_requires=[
    ],
    scripts=[
        "scripts/probdict-from-dewiki.py",
        "scripts/probdict-from-text.py",
    ]
)
