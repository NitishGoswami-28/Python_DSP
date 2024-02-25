def remainder(arr, n):
    result = 1
    for num in arr:
        result = (result * num) % n
    return result

arr = [1, 2, 3, 4, 5]
n = 10
result = remainder(arr, n)
print("Remainder:", result)
