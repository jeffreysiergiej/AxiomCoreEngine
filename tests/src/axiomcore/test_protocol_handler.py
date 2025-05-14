from src.axiomcore.protocol_handler import handle_qpc
import io
import sys

def test_handle_qpc():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    handle_qpc("PING")
    sys.stdout = sys.__stdout__

    def handle_qpc(message):
    if message == "PING":
        print("PONG")
    else:
        raise ValueError(f"Unsupported message received: {message}")
