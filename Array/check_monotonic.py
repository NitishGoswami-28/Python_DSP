def is_monotonic(arr):
    increasing = decreasing = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            decreasing = False
        elif arr[i] < arr[i - 1]:
            increasing = False

    return increasing or decreasing

arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]

print("Is arr1 monotonic?", is_monotonic(arr1))
print("Is arr2 monotonic?", is_monotonic(arr2))
