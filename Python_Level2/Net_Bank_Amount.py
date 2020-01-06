d_amount=0
w_amount=0
while True:
    s=input()
    if s:
        t=s.split(" ")
        if t[0]=="D":
            d_amount+=int(t[1])
        elif t[0]=="W":
            w_amount+=int(t[1])
    else:
        break
print(d_amount-w_amount)
            
            
            
    
