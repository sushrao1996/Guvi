class toys():
    count=0

    def count_func(self):
        toys.count+=1
t = toys()
print(t.count)
t.count_func()
print(t.count)
