import array as ar
a=ar.array('i',[])
b=ar.array('i',[])
c=ar.array('i',[])
size=int(input("Enter the size of the array : "))
print("Enter the elements for array1 : ")
for i in range(size):
    a.append(int(input()))
for i in a:
    if i%2==0:
        b.append(i)
    else:
        c.append(i)
print("Sorted Even Elements: ")
for i in range(len(b)):
    for j in range(i+1,len(b)):
        if b[i]>b[j]:
            temp=b[i]
            b[i]=b[j]
            b[j]=temp
for i in b:
    print(i,end=" ")
print("\n")
print("Sorted Odd Elements: ")
for i in range(len(c)):
    for j in range(i+1,len(c)):
        if c[i]>c[j]:
            temp=c[i]
            c[i]=c[j]
            c[j]=temp
for i in c:
    print(i,end=" ")
