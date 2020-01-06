s=input()
u_count=0
l_count=0
for i in s:
    if i>'a' and i<'z':
        l_count+=1
    elif i>'A' and i<'Z':
        u_count+=1
print("UPPER CASE",u_count)
print("LOWER CASE",l_count)
        
    
