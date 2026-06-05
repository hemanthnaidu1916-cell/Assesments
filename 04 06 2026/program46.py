def happy(n):
    while n != 1 and n != 4:
        s = 0
        while n > 0:
            d = n % 10
            s += d * d
            n //= 10
        n = s
    return n == 1

print("Happy numbers between 1 and 100 are:")
for i in range(1, 101):
    if happy(i):
        print(i, end=" ")
