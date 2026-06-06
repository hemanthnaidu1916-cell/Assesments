num = [10, 5, 20, 3, 15]

largest = second = -1

for i in num:
    if i > largest:
        second = largest
        largest = i
    elif i > second:
        second = i

print("Second largest number =", second)
