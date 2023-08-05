"""Run upon call of pip install ml-tools."""

from pathlib import Path

from setuptools import find_packages, setup

here = Path(__file__).parent
name = "cri-ml-tools"

setup(
    name=name,
    # packages=find_packages(),
    # version="0.0.0",
)
