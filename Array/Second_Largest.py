import array as ar
a=ar.array('i',[])
size=int(input("Enter the size of the array : "))
for i in range(size):
    a.append(int(input()))
max=a[0]
for i in range(0,len(a)):
    if a[i]>max:
        max=a[i]
index=a.index(max)
a.pop(index)
second_max=a[0]
for i in range(0,len(a)):
    if a[i]>max:
        second_max=a[i]
print(second_max)
