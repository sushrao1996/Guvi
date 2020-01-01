def cube_function(num):
    a=1
    a*=num*num*num
    return a
num_input=int(input("Enter a number whose cube has to be found : "))
print(cube_function(num_input))
