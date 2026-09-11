def safe_insert(arr, idx, val):
    if idx < 0:
        arr.insert(0, val)
    elif idx >= len(arr):
        arr.append(val)
    else:
        arr.insert(idx, val)
