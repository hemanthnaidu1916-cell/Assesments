def is_disarium(num):
    digits = str(num)
    total = 0

    for i in range(len(digits)):
        total += int(digits[i]) ** (i + 1)

    return total == num


print("Disarium numbers between 1 and 100 are:")

for i in range(1, 101):
    if is_disarium(i):
        print(i)
