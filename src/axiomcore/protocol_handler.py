import io, sys

def handle_qpc(command: str):
    print("PONG") if command == "PING" else print("UNKNOWN")

def handle_qpc(message):
    if message == "PING":
        print("PONG")
    elif message == "STATUS":
        print("ALIVE")
    else:
        raise ValueError(f"Unsupported message received: {message}")
