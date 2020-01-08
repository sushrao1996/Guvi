import re
s=input()
l=s.split(",")
l1=[]
print(l)
for j in l:
    if len(j)<6 or len(j)>12:
        flag=-1
        break
    elif not re.search("[a-z]",j):
        flag=-1
        break
    elif not re.search("[A-Z]",j):
        flag=-1
        break
    elif not re.search("[0-9]",j):
        flag=-1
        break
    elif not re.search("[$#@]",j):
        flag=-1
        break
    else:
        flag=0
        l1.append(j)
print(",".join(l1))
