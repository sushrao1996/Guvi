a=int(input("Enter the amount : "))
if a>1000:
    b=int(a/1000)
    print("1000 : " + str(b))
    a=a-(b*1000)
if a>500:
    c=int(a/500)
    print("500 : " + str(c))
    a=a-(c*500)
if a>200:
    d=int(a/200)
    print("200 : " + str(d))
    a=a-(d*200)
if a>100:
    e=int(a/100)
    print("100 : " + str(e))
    a=a-(e*100)
if a>50:
    f=int(a/50)
    print("50 : " + str(f))
    a=a-(f*50)
if a>20:
    g=int(a/20)
    print("20 : " + str(g))
    a=a-(g*20)
if a>10:
    h=int(a/10)
    print("10 : " + str(h))
    a=a-(h*10)
print(str(a)+ " amount is available in coins.")
