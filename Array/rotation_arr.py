arr = [1,2,3,4,5,6,7,8]

rot = int(input("Enter the number of rotation: "))
print("The original array: ", arr)
for _ in range(rot):
    a = arr[0]
    arr.pop(0)
    arr.append(a)
    
print("The rotated arr is: ", arr)