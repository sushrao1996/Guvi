a=input("Enter a number : ")
b=[]
c=""
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
for i in b:
    c+=i
if a==c:
    print (a + " is a palindrome number.")
else:
    print (a + " is not a palindrome number.")
    
    
