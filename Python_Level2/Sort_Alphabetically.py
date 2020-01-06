n=input("Enter the words : ")
l=n.split(",")
l.sort()
print(l)
for i in range(len(l)):
    if i==len(l)-1:
        print(l[i],end="")
    else:
        print(l[i],end=",")
