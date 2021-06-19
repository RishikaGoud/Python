a = [1,4,7]

#appending list a
a.append(45) 
print(a)

#extending list a
a.extend([8,10])
print(a)

#inserting element into list
a.insert(4,7)
print(a)

#copying list a
b = a.copy()
print(b)

#counting elements in list b
x = b.count(7)
print(x)

#index value
x = b.index(45)
print(x)

#removing element from list a
a.remove(4)
print(a)

#sorting list b
b.sort()
print(b)

#reversing the order of list b
b.reverse()
print(b)

#popping element from list a
a.pop(1)
print(a)

#clearing list a and b
a.clear()
b.clear()
print(a)
print(b)
