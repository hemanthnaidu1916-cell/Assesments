def list_operation(x, y, n):
    return [i for i in range(x, y + 1) if i % n == 0]
print(list_operation(1, 10, 3))

print(list_operation(7, 9, 2))

print(list_operation(15, 20, 7))
