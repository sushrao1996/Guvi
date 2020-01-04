import array as ar
a=ar.array('i',[])
b=ar.array('i',[])
d=ar.array('i',[])
size=int(input("Enter the size of the array : "))
print("Enter the elements : ")
for i in range(size):
    a.append(int(input()))
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    c=0
    for j in range(len(a)):
        if i==a[j]:
            c+=1
    if c>1:
        d.append(i)
print("Count of duplicate elements : ",len(d))
    
        
            
