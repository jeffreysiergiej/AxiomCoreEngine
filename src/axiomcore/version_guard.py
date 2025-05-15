import sys

REQUIRED_MAJOR = 3
REQUIRED_MINOR = 11

def enforce_version():
    if sys.version_info < (REQUIRED_MAJOR, REQUIRED_MINOR):
        raise RuntimeError(
            f"AxiomCoreEngine requires Python {REQUIRED_MAJOR}.{REQUIRED_MINOR}+ "
            f"but detected Python {sys.version_info.major}.{sys.version_info.minor}. "
            "Please upgrade your interpreter."
        )
