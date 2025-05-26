
from setuptools import setup, find_packages

setup(
    name="optuna_tpe_suggestion",
    version="0.1",
    packages=find_packages(),  # will now find the actual package
    install_requires=["optuna", "numpy"],
    python_requires=">=3.7",
    zip_safe=True,
)