from collections import OrderedDict

def check_order(s, pattern):
    od = OrderedDict.fromkeys(s)
    return ''.join(od.keys()) == pattern

result = check_order('hello', 'heo')
print(result)
