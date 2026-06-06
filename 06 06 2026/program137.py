def equal(a, b, c):
    return 3 - len({a, b, c})
print(equal(3, 4, 3))
print(equal(1, 1, 1))   
print(equal(3, 4, 1))   
