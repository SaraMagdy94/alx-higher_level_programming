#!/usr/bin/python3

# Example script to demonstrate magic_calculation

def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    else:
        return a * b - c


# Call magic_calculation with some example values
result = magic_calculation(2, 3, 4)
print(result)
