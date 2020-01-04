import array as ar
a=ar.array('i',[])
size=int(input("Enter the size of the array : "))
print("Enter the elements : ")
for i in range(size):
    a.append(int(input()))
pos=int(input("Enter the position at which the element has to be deleted : "))
a.pop(pos)
print("Elements in the array after deletion : ")
for i in a:
    print(i,end=" ")
