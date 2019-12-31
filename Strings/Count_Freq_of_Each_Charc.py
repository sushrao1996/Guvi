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
dict={}
for i in range(0,len(l)):
    for j in range(0,len(l1)):
        if i==j:
            dict[l[i]]=l1[j]
        else:
            pass
print(dict)
