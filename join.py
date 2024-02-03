def join_tuples(tuples):
    result = []
    current_tuple = None


    for t in tuples:
        if current_tuple is None:
            current_tuple = t
        elif current_tuple[0] == t[0]:
            current_tuple += t[1:]
        else:
            result.append(current_tuple)
            current_tuple = t


    if current_tuple is not None:
        result.append(current_tuple)

    return result


input_tuples = [(1, 'apple'), (1, 'banana'), (2, 'orange'), (3, 'grape'), (3, 'kiwi')]
joined_tuples = join_tuples(input_tuples)

print("Original tuples:", input_tuples)
print("Joined tuples:", joined_tuples)
