import array as ar
a=ar.array('i',[])
size=int(input("Enter the size of the array : "))
print("Enter the elements : ")
for i in range(size):
    a.append(int(input()))
search_element=int(input("Enter the number to be searched in the array : "))
def search_func(a,s):
    if i in a:
        print("The number is available in the array.")
        return
    else:
        print("The number is not available in the array.")
        return
search_func(a,search_element)
