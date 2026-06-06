from collections import OrderedDict
od = OrderedDict({
    'b': 2,
    'c': 3,
    'd': 4
})

od['a'] = 1
od.move_to_end('a', last=False)

print("OrderedDict after insertion at the beginning:")
print(od)
