import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--km", type=float, required=True)
    a = p.parse_args()
    miles = a.km * 0.621371
    print(f"{miles:.2f}")
