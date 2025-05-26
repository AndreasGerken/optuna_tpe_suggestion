
from setuptools import setup, find_packages

setup(
    name="optuna_tpe_suggestion",
    author="Lars Andersen Bratholm",
    version="0.1",
    packages=find_packages(),
    install_requires=["optuna", "numpy"],
    python_requires=">=3.7",
    zip_safe=True,
)