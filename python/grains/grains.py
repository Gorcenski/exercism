def on_square(integer_number):
    if integer_number <= 0 or integer_number > 64:
        raise ValueError("This square not found on a chess board!")
    return 1 << integer_number - 1


def total_after(integer_number):
    if integer_number <= 0 or integer_number > 64:
        raise ValueError("This square not found on a chess board!")
    return 2**integer_number - 1
    pass
