#iterator design pattern

# data=[10,20,30,40]
# print(data[2])
# for i in data:
#     print(i) #build in iterator

# d=iter(data)
# print(type(d))
# print(d.__next__())
# print(d.__next__())
# print(next(d))
# print(next(d))
# print(next(d))

#panda.head() give by default 5 of top in a file
#panda.tail() give by default 5 of bottom in a file
#now how to create your custom iterator

class Head:
    def __init__(self):
        self.num = 1  # No changes here

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= 5:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
        
#--------------------------------
values = Head()  # Removed (100), as Head() doesn't take arguments
print(values.__next__())
print(values.__next__())

values = Head()  # Removed (100) again
for i in values:
    print(i)  # Built-in iterator
