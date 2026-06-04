for num in range(1, 1000):
    s = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        s += digit ** 3
        temp //= 10

    if num == s:
        print(num)
