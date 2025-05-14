import pytest

@pytest.fixture
def sample_input():
    return {"message": "PING"}

@pytest.fixture
def reset_stdout(monkeypatch):
    import sys
    from io import StringIO
    stream = StringIO()
    monkeypatch.setattr(sys, 'stdout', stream)
    return stream
