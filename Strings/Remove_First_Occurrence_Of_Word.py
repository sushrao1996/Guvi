a=input("Enter a string : ")
b=input("Enter a word whose first occurence has to be removed : ")
d=a.split(" ")
e=""
for i in range(len(d)):
    if b==d[i]:
        c=i
        break
for i in range(0,c):
    e=e+d[i]+" "
for j in range(c+1,len(d)):
    e=e+d[j]+" "
print(e)

         
