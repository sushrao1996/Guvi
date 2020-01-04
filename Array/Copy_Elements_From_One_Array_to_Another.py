import array as ar
a=ar.array('i',[])
size=int(input("Enter the size of the array : "))
print("Enter the elements : ")
for i in range(size):
    a.append(int(input()))
arr=[]*len(a)
for i in a:
    arr.append(i)
for i in arr:
    print(i,end=" ")
