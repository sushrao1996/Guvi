Vowels=('a','e','i','o','u')
a=input("Enter a string : ")
a=a.lower()
vowel_count=0
consonant_count=0
for i in a:
    if i in Vowels:
        vowel_count+=1
    elif i>'a' and i<'z':
        consonant_count+=1
print("Number of Vowels : ",vowel_count)
print("Number of Consonants : ",consonant_count)
    
