num = int(input("Enter a number: "))

if num > 1 and all(num % i != 0 for i in range(2, num)):
    print("Prime Number")
else:
    print("Not a Prime Number")
