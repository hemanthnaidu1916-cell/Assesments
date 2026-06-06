def multiply_nums(s):
    nums = map(int, s.split(", "))
    product = 1

    for num in nums:
        product *= num

    return product
print(multiply_nums("2, 3"))           
print(multiply_nums("1, 2, 3, 4"))     
print(multiply_nums("54, 75, 453, 0")) 
print(multiply_nums("10, -2"))         
