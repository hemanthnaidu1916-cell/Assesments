def move_to_end(lst, elem):
    result = [x for x in lst if x != elem]   # all other elements
    result.extend([x for x in lst if x == elem])  # all target elements at end
    return result

print(move_to_end([1, 3, 2, 4, 4, 1], 1))
print(move_to_end([7, 8, 9, 1, 2, 3, 4], 9))
print(move_to_end(["a", "a", "a", "b"], "a"))
