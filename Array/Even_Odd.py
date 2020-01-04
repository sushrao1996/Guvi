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
print("Even Elements: ")
for i in b:
    print(i,end=" ")
print("\n")
print("Odd Elements: ")
for i in c:
    print(i,end=" ")

