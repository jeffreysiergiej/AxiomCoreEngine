from dotenv import load_dotenv
import os

def load_environment():
    load_dotenv()
    print("PYTHONPATH is set to:", os.getenv("PYTHONPATH"))

def handle_qpc(message):
    """Respond to basic QPC protocol messages."""
    if not isinstance(message, str):
        raise TypeError("Message must be a string")

    response = None

    if message.upper() == "PING":
        response = "PONG"
        elif message.upper() == "STATUS":
        response = "CORE STABLE"
    else:
        response = "UNKNOWN COMMAND"

    return response
