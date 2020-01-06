a=input()
l=a.split(",")
l1=[]
for i in l:
    j=int(i,2)
    if j%5==0:
        l1.append(i)
print(','.join(l1))
