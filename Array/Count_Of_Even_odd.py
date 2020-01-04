import array as ar
a=ar.array('i',[])
size=int(input("Enter the size of the array : "))
for i in range(size):
    a.append(int(input()))
c_even=0
c_odd=0
for i in a:
    if i%2==0:
        c_even+=1
    else:
        c_odd+=1
print("Total number of even elements : ",c_even)
print("Total number of even elements : ",c_odd)       
