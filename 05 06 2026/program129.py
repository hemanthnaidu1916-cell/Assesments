def square_digits(num):
    return int(''.join(str(int(digit) ** 2) for digit in str(num)))
print(square_digits(9119))  
print(square_digits(2483))  
print(square_digits(3212))  
