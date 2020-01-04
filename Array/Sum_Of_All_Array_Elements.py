import array as ar
a=ar.array('i',[])
size=int(input("Enter the size of the array : "))
for i in range(size):
    a.append(int(input()))
sum=0
for i in a:
    sum+=i
print(sum)
