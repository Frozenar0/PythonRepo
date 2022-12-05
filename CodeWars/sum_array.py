def sum_array(arr):

    if arr is None or len(arr) < 3:
        return 0
    else:
        arr.remove(max(arr))
        arr.remove(min(arr))
        return sum(arr)

print((sum_array(None)))
print((sum_array([])))
print((sum_array([-3])))
print((sum_array([-3-5])))