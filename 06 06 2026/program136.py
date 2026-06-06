def is_triplet(a, b, c):
    nums = sorted([a, b, c])
    return nums[0]**2 + nums[1]**2 == nums[2]**2
print(is_triplet(3, 4, 5))     
print(is_triplet(13, 5, 12))   
print(is_triplet(1, 2, 3)) 
