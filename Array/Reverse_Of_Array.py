import array as ar
a=ar.array('i',[])
b=ar.array('i',[])
size=int(input("Enter the size of the array : "))
print("Enter the elements for array1 : ")
for i in range(size):
    a.append(int(input()))
for i in range(len(a)-1,-1,-1):
    print(a[i],end=" ")
