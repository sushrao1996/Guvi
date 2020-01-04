import array as ar
a=ar.array('i',[])
size=int(input("Enter the size of the array : "))
print("Enter the elements : ")
for i in range(size):
    a.append(int(input()))
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("Elements in ascending order  : ")
for i in a:
    print(i,end=" ")
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print("\n")
print("Elements in descending order  : ")
for i in a:
    print(i,end=" ")
