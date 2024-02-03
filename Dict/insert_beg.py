from collections import OrderedDict

my_ordered_dict = OrderedDict([('a', 1), ('b', 2)])
my_ordered_dict.update({'c': 3})
my_ordered_dict.move_to_end('c', last=False)
print(my_ordered_dict)
