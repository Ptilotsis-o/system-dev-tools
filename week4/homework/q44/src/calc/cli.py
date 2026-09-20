import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--op", choices=["add", "sub"], required=True)
    p.add_argument("--a", type=float, required=True)
    p.add_argument("--b", type=float, required=True)
    args = p.parse_args()
    if args.op == "add":
        result = args.a + args.b
    else:
        result = args.a + args.b   # 故意缺陷：减法写成了加法
    print(result)
