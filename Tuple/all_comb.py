def all_pairs(tuple1, tuple2):
    combinations = []

    for item1 in tuple1:
        for item2 in tuple2:
            combinations.append((item1, item2))

    return combinations

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

combinations = all_pairs(tuple1, tuple2)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("All pair combinations:", combinations)
