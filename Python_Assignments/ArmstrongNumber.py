a=input("Enter a number : \n")
l=[]
for i in a:
	l.append(i)
l1=[]
for i in l:
    i=int(i)
    l1.append(i)
b=0
for i in l1:
    b += i*i*i
if (int(a)==b):
	print( str(a) + " is an Armstrong Number")
else:
	print(str(a) + " is not an Armstrong Number")
