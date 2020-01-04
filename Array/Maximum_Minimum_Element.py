import array as ar
a=ar.array('i',[])
size=int(input("Enter the size of the array : "))
for i in range(size):
    a.append(int(input()))
max=a[0]
min=a[0]
for i in range(0,len(a)):
    if a[i]>max:
        max=a[i]
print("Maximum Element : ",max)
for i in range(0,len(a)):
    if a[i]<min:
        min=a[i]
print("Minimum Element : ",min)
