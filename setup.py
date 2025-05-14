from setuptools import setup, find_packages

setup(
    name="AxiomCoreEngine",
    version="1.0.0",
    description="Scalar AI Architecture Runtime",
    author="Jeffrey Siergiej",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11,<3.12",
    install_requires=[
        "numpy",
        "matplotlib",
        "scipy",
        "pandas",
        "notebook",
        "ipython",
        "pytest",
        "bandit",
    ],
)
