"""Run upon call of pip install ml-tools."""

from pathlib import Path

from setuptools import setup

here = Path(__file__).parent
name = "cri-data-tools"

setup(name=name, version="0.0.0dev0")
