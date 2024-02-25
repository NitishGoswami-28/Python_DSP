seen = set()
duplicates = set()
lst = [1, 2, 3, 1, 5, 6, 1, 3]

for item in lst:
        if item in seen_set:
            duplicates.add(item)
        else:
            seen.add(item)

print("Duplicate values: ", list(duplicates_set))

