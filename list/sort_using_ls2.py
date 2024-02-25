list1 = [4, 2, 8, 1, 6]
list2 = [3, 1, 4, 2, 5]
sorted_values = [value for _, value in sorted(zip(list2, list1))]

print("list1:", list1)
print("list2:", list2)
print("Sorted list1:", sorted_values)