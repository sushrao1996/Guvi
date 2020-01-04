import array as ar
a=ar.array('i',[])
size=int(input("Enter the size of the array : "))
print("Enter the elements for array : ")
for i in range(size):
    a.append(int(input()))
n=int(input("Enter the number of times the array should be left rotated :"))
c=a[n:]+a[:n]
for i in c:
    print(i,end=" ")
