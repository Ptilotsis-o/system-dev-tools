from safe_insert import safe_insert

def test_append(): 
    arr = [1,2,3]
    safe_insert(arr, 5, 99); assert arr == [1,2,3,99]
