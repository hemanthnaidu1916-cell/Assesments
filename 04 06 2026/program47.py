n = int(input("Enter a number: "))
temp = n
digit_sum = 0

while temp > 0:
    digit_sum += temp % 10
    temp //= 10

if n % digit_sum == 0:
    print(n, "is a Harshad Number")
else:
    print(n, "is not a Harshad Number")
