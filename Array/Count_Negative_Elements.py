import array as ar
a=ar.array('i',[])
size=int(input("Enter the size of the array : "))
print("Enter the elements : ")
for i in range(size):
    a.append(int(input()))
c=0
for i in a:
    if i<0:
        c+=1
print("Total Number of negative elements in the array are : ",c)
        
