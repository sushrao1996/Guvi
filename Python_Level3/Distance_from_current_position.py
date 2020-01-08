pos=[0,0]
while True:
    s=input()
    if not s:
        break
    l=s.split(" ")
    direction= l[0]
    steps =int(l[1])
    if direction=="UP":
        pos[0]+=steps
    elif direction=="DOWN":
        pos[0]-=steps
    elif direction=="LEFT":
        pos[1]-=steps
    elif direction=="RIGHT":
        pos[1]+=steps
    else:
        pass
distance=pos[1]**2+pos[0]**2
distance=round(distance**0.5)
print("Distance :",int(distance))
 
