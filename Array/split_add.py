def split_and_add(arr,k):
    n = len(arr)
    arr[:] = arr[k % n:] + arr[:k % n]

arr = [1, 2, 3, 4, 5, 6, 7]
split_and_add(arr, 3)
print("Modified array:", arr)