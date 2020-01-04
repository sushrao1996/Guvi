import array as ar
a=ar.array('i',[])
size=int(input("Enter the size of the array : "))
print("Enter the elements for array : ")
for i in range(size):
    a.append(int(input()))
n=int(input("Enter the number of times the array should be right rotated :"))
r=len(a)-n
c=a[r:]+a[:r]
for i in c:
    print(i,end=" ")
    
