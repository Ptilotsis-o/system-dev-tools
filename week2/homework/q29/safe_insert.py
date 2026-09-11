def safe_insert(arr, idx, val):
    if idx < 0 or idx > len(arr):
        raise IndexError("Index out of range")   # 故意在这里抛出
    arr.insert(idx, val)

safe_insert([1,2,3], 5, 99)   # 触发异常
