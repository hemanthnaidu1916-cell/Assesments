def missing_num(lst):
    return sum(range(1, 11)) - sum(lst)

print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))
print(missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]))
print(missing_num([10, 5, 1, 2, 4, 6, 8, 3, 9]))
