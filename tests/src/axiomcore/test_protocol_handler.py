from src.axiomcore.protocol_handler import handle_qpc
import io
import sys

def test_handle_qpc():
    captured_output = io.StringIO()
    sys.stdout = captured_output
    handle_qpc("PING")
    sys.stdout = sys.__stdout__

    output = captured_output.getvalue()
    if "PONG" not in output and output.strip() == "":
        raise AssertionError("Expected output missing from handle_qpc")
