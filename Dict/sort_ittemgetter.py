from operator import itemgetter

list_of_dicts = [{'a': 3, 'b': 2}, {'a': 1, 'b': 4}, {'a': 2, 'b': 3}]
sorted_list = sorted(list_of_dicts, key=itemgetter('b'))
print(sorted_list)
