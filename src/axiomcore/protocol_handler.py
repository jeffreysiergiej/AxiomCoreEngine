import io, sys

def handle_qpc(command: str):
    print("PONG") if command == "PING" else print("UNKNOWN")

def handle_qpc(message):
    if message == "PING":
        print("PONG")
    else:
        raise ValueError(f"Unsupported message received: {message}")
