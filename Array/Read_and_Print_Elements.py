import array as ar
a=ar.array('i',[])
size=int(input("Enter the size of array : "))
print("Enter the elements of the array : ")
for i in range(size):
    a.append(int(input()))
print("Elements are : ")
for i in a:
    print(i,end=",")
    
