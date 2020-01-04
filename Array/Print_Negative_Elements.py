import array as ar
a=ar.array('i',[])
size=int(input("Enter the size of the array : "))
for i in range(size):
    a.append(int(input()))
print("Negative Elements in the array are : ")
for i in a:
    if i<0:
        print(i,end=" ")
        
