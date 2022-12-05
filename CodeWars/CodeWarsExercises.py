def sum_array(arr):
    #your code here

     if int(len(arr)) < 2:
         return 0
     else:
        arr.remove(max(arr))
        arr.remove(min(arr))
        return sum(arr)

print(sum_array(0))