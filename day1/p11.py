"""
Check if a string is a palindrome
"""

num=input("Enter string: ")

count=len(num)
flag=True
for i in range(count):
   if(num[i]==num[(count-1)-i]):
      flag=True
   else:
      flag=False
    
if(flag==True):
   print("string is a palindrome")
else:
   print("string is not a palindrome")

      







