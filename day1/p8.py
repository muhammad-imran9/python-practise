"""
Check if a number is prime
"""

num=int(input("Enter a number: "))

count=0
for i in range(num):
    if(num%(i+1)==0):
        count=count+1

if (count==2):
    print(f"{num} is prime number")
else:
    print(f"{num} is not a prime number")
