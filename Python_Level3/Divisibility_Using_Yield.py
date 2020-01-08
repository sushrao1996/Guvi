class divisibility():
    def div_by_seven(self,n):
        i=0
        while i<n:
            j=i
            i=i+1
            if j%7==0:
                yield j
d=divisibility()

for i in d.div_by_seven(100):
    print(i)
