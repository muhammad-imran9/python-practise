"""
Print the sum of first N natural numbers
"""

num=int(input("Enter a number: "))

sum=0
for i in range(num):
    sum=sum+(i+1)

print(f"sum of first {num} natural  number is {sum}")