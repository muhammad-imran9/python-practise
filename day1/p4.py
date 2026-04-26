"""
Swap two variables without using a third variable
"""

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

print("Before swap")
print(f"num1 is {num1} num2 is {num2}")

num1,num2=num2,num1

print("After swap")
print(f"num1 is {num1} num2 is {num2}")