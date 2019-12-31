a=input("Enter a string : ")
l=[]
l1=[]
for i in a:
    l.append(i)
for i in range(0,len(l)):
    c=0
    for j in range(i,len(l)):
        if l[i]==l[j]:
            c+=1
    l1.append(c)
l2=[]
for i in range(0,len(l1)):
    if max(l1)==l1[i]:
        l2.append(i)
print("Highest Frequency Character is : ")
for i in l2:
    print(l[i])
