import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--text", required=True)
    a = p.parse_args()
    print(a.text[::-1])
