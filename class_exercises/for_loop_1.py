batches=["21cys","22cys","23cys",]
for i in batches:
    print(i)
print(len(batches))
print(batches[-1])
print(batches[len(batches)-1])
a=[1,2,3,4,232]
print(a[:2])
print(a[2:4])
for i in a:
    print(i)
print("---------------")
print(a[3:8])
a.append(43)
for i in a:
    print(i)
print("---------------")
a[3]=29                 #adding an element directly using index
for i in a:
    print(i)            
print("---------------")
print(len(a))
a.insert(4,25)
a.insert(5,25)
print("LIST : ",a)
print("---------------")
print(a.count(25))
print(a[5])
a.pop(5)                #removing an element, uses the index of the element
print("Pop : ",a)
a.remove(25)            #removing an element, uses the element
print(a)
a.insert(4,25)          #inserting an element
print(a)
del a[4]                #deleting an element
print(a)
a.sort()                #sorting an arry
print(a)
a.reverse()             #reversing an array
print(a)
a.sort(reverse=True)    #sorting and reversing
xyz=a                   #copying a list
print("COPY : ",xyz)
a[0]=34
print(a)
print(xyz)              #both list (xyz, a) have same memory allocation
abc=list(a)             #inspite of both the lists having the elements, but are stored in diffrent memory location
print(a)
my_neighbours=[30]
print(my_neighbours)
my_neighbours.append(31)
print(my_neighbours)
my_neighbours.insert(2,32)
print(my_neighbours)
my_neighbours.insert(0,29)
print(my_neighbours)
my_neighbours.insert(0,28)
print(my_neighbours)
my_neighbours.insert(0,27)
print(my_neighbours)
my_neighbours.insert(0,26)
print(my_neighbours)
my_neighbours.append(33)
print(my_neighbours)
my_neighbours.remove(29)
print(my_neighbours)

