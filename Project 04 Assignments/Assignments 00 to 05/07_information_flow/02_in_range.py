def in_range(n, low, high):
    if n >= low and n <= high:
        return True

    # we could have also included an else statement, but since we are returning, it's fine without!
    return False

print(in_range(5, 1, 10))