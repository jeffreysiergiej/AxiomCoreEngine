from src.axiomcore.protocol_handler import handle_qpc

def test_handle_qpc():
    result = handle_qpc("PING")
    assert result == "PONG"
