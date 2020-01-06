s=input()
a_count=0
d_count=0
for i in s:
    if i.isalpha():
        a_count+=1
    elif i.isdigit():
        d_count+=1
print("LETTERS",a_count)
print("DIGITS",d_count)
        
