import array as ar
a=ar.array('i',[])
size=int(input("Enter the size of the array : "))
print("Enter the elements : ")
for i in range(size):
    a.append(int(input()))
insert_element=int(input("Enter the element to be inserted : "))
pos=int(input("Enter the position at which the element has to be inserted : "))
a.insert(pos,insert_element)
for i in a:
    print(i,end=" ")
