from collections import defaultdict

nested_tuple = (('key1', 'abc1', 'value1'),
               ('key1', 'abc2', 'val2'),
               ('key2', 'xyy', 'val3'))

nested_dict = defaultdict(dict)
for key, subkey, value in nested_tuple:
        nested_dict[key][subkey] = value


print("Original nested tuple:", nested_tuple)
print("Converted nested dictionary:", dict(nested_dict))
