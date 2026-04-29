"""
Reverse a number (e.g., 123 → 321)
"""

num=int(input("Enter a number: "))

count=len(str(num))
counts=[]

for i in range(count):
    counts.append(num%10)
    num=int(num/10)

for i in range(count):
    print(f"{counts[i]}")





