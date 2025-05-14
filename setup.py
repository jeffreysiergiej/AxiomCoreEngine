from setuptools import setup, find_packages

setup(
    name="AxiomCoreEngine",
    version="1.0.0",
    description="Scalar AI Architecture Runtime",
    author="Jeffrey Siergiej",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[],
    python_requires=">=3.11.*"
)
