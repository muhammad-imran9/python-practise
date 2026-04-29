"""
Count vowels and consonants in a string
"""

text=input("Enter text: ")

vowel=0
constant=0
for i in range(len(text)):
    if(text[i]=='a' or text[i]=='e' or text[i]=='i' or text[i]=='o' or text[i]=='u'):
        vowel=vowel+1
    else:
        constant=constant+1
    if(text[i]==' '):
         constant=constant-1


print(vowel)
print(constant)


