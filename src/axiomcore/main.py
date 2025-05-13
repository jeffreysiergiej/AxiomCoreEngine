def add_two_numbers(a, b):
    """Securely add two numbers"""
    try:
        return int(a) + int(b)
    except (ValueError, TypeError):
        return 0
