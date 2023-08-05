"""Run upon call of pip install ml-tools."""

from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).parent
name = "cri-ml-tools"

setup(name=name, version="0.0.0.dev0")
