import sys

def divide(a, b):
    if b == 0:
        print("division by zero", file=sys.stderr)
        return None
    return a / b
