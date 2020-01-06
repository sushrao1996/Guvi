size=int(input("For how many numbers the factorial has to be found : "))
print("Enter the numbers : ")
l=[]
for i in range(size):
    l.append(int(input()))
l1=[]
for i in l:
    if i==0:
        l1.append(1)
    else:
        b=1
        for j in range(i,0,-1):
            b*=j
        l1.append(b)
for i in range(len(l1)):
    if i!=len(l1)-1:
        print(l1[i],end=",")
    else:
        print(l1[i],end=".")
            
        
