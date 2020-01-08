import operator
dict={}
s=input()
l=s.split(" ")
for i in l:
    dict[i]=l.count(i)
for i,j in sorted(dict.items()):
    print (i,":",j)
