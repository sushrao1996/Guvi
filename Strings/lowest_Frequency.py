a=input("Enter a string : ")
l=[]
l1=[]
for i in a:
    l.append(i)
for i in range(0,len(l)):
    c=0
    for j in range(0,len(l)):
        if l[i]==l[j]:
            c+=1
    l1.append(c)
l2=[]
for i in range(0,len(l1)):
    if l1[i]==min(l1):
        l2.append(i)
print("Lowest Frequency Character :")
for i in l2:
    print(l[i])
