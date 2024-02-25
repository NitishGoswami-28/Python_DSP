def rotate_array(arr, d):
    n = len(arr)
    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


arr = [1, 2, 3, 4, 5, 6, 7]
rotate_array(arr, 2)
print("Rotated array:", arr)
