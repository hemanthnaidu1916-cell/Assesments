def mean(num):
    digits = [int(d) for d in str(num)]
    return sum(digits) // len(digits)
print(mean(42))     
print(mean(12345))  
print(mean(666))    
