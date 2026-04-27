"""
Print the factorial of a number
"""
num=int(input("Enter a number: "))

product=1
sum=0
for i in range(num,1,-1):
    product=product*(i)
    
print(f"factorial of a {num} is {product}") 