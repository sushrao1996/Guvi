a=input("Enter a binary number : ")
b=[]
for i in a:
    if int(i)==0:
        b.append(1)
    elif int(i)==1:
        b.append(0)
    else:
        print("Please enter a binary number")
c=[]
if 0 not in b:
    print("2's complement of " + a + " is 1" + str(a))
else:
    for j in range(len(b)-1,-1,-1):
        if b[j]==1:
            c.append(0)
        elif b[j]==0:
            c.append(1)
            for k in range((len(b)-len(c))-1,-1,-1):
                c.append(b[k])
            break
for i in range(len(c)-1,-1,-1):
    print(c[i],end="")
        

