import pytest

@pytest.fixture(scope="session")
def sample_config():
    return {"boot_mode": "safe", "debug": True}
