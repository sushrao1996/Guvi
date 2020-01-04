import array as ar
a=ar.array('i',[])
b=ar.array('i',[])
size=int(input("Enter the size of the array : "))
print("Enter the elements for array1 : ")
for i in range(size):
    a.append(int(input()))
size1=int(input("Enter the size of the array : "))
print("Enter the elements for array2: ")
for i in range(size1):
    b.append(int(input()))
c=a+b
for i in c:
    print(i,end=" ")
