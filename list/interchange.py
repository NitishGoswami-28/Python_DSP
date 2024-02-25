arr = [1,23,45,78,54]

print("The original array: ", arr)

arr[0] = arr[0] + arr[len(arr)-1]
arr[len(arr)-1] = arr[0] - arr[len(arr)-1]
arr[0] = arr[0]- arr[len(arr)-1]

print("Array after interchaging: ", arr)