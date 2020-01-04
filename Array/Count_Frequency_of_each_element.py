import array as ar
a=ar.array('i',[])
size=int(input("Enter the size of the array : "))
print("Enter the elements : ")
for i in range(size):
    a.append(int(input()))
freq_element=int(input("Enter the element whose frequency in the array has to be found : "))
#method1
c=0
for i in range(len(a)):
    if a[i]==freq_element:
        c+=1
print("Frequency of the above element is: ",c)

#method2
#c=a.count(freq_element)
#print("Frequency of the above element is: ",c)
               
