bill=float(input("Enter the bill amount: "))
if bill>10000:
    discount=30
    discount_amount=(bill*discount)/100
    final_amount=bill-discount_amount
elif bill>5000:
    discount=20
    discount_amount=(bill*discount)/100
    final_amount=bill-discount_amount
else:
    discount=0
    discount_amount=0
    final_amount=bill
print("--- Bill Summary---")
print(f"Original Amount : {bill:.2f}")
print(f"Discount    :{discount}% ({discount_amount:.2f})")
print(f"Final Amount : {final_amount:.2f}")
