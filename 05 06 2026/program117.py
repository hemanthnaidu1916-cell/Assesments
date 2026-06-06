def next_in_line(lst, num):
    if len(lst) == 0:
        return "No list has been selected"
    
    lst.append(num)   
    lst.pop(0)        
    return lst


print(next_in_line([5, 6, 7, 8, 9], 1))
print(next_in_line([7, 6, 3, 23, 17], 10))
print(next_in_line([1, 10, 20, 42], 6))
print(next_in_line([], 6))
