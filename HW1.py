def sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  
        j = i - 1
      
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

       
        arr[j + 1] = key

    return arr




arr = [2, 30, 1, 25, 5, 9]
sorted_arr = sort(arr)

print(sorted_arr)