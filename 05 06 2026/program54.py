def n_largest_elements(lst, n):
    return sorted(lst, reverse=True)[:n]

numbers = [10, 4, 3, 50, 23, 90]
print(n_largest_elements(numbers, 3))
