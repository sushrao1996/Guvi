import array as ar
a=ar.array('i',[])
b=ar.array('i',[])
size=int(input("Enter the size of the array : "))
print("Enter the elements : ")
for i in range(size):
    a.append(int(input()))
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    print(i,end=" ")
