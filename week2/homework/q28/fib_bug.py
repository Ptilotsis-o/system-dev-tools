def fib(n):
    if n < 2:        # 错误
        return 1
    return fib(n-1) + fib(n-2)

print(fib(0))
