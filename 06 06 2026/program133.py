from collections import Counter

def unique(lst):
    counts = Counter(lst)
    for num, count in counts.items():
        if count == 1:
            return num
print(unique([3, 3, 3, 7, 3, 3]))          
print(unique([0, 0, 0.77, 0, 0]))          
print(unique([0, 1, 1, 1, 1, 1, 1, 1]))            
