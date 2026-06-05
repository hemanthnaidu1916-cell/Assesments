n = int(input("Enter a number: "))
original = n
seen = set()

while n != 1 and n not in seen:
    seen.add(n)
    s=0
    while n>0:
        digit=n%10
        s+=digit**2
        n//=10
    n=s
if n==1:
    print(original, "is a Happy Number")
else:
    print(original, "is not a Happy Number")
    
