def handle_qpc(message):
    """Respond to basic QPC protocol messages."""
    if not isinstance(message, str):
        raise TypeError("Message must be a string")

    response = None

    if message.upper() == "PING":
        response = "PONG"
    elif message.upper() == "STATUS":
        response = "ALIVE"
    else:
        raise ValueError(f"Unsupported message received: {message}")

    print(response)
    return response
