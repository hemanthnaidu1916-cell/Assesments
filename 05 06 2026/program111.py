def find_even_nums(n):
    return [i for i in range(1, n + 1) if i % 2 == 0]

print(find_even_nums(8))
print(find_even_nums(4))
print(find_even_nums(2))
