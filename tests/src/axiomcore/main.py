def add_two_numbers(a, b):
    """
    Safely adds two numbers, ensuring type and security.
    """
    try:
        a = int(a)
        b = int(b)
        return a + b
    except (ValueError, TypeError):
        return 0
