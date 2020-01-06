n=input()
l=n.split(",")
l1=[i for i in l if int(i)%2!=0]
print(",".join(l1))
    
