a = {"name" : "rishi", "age" : 19, "occupation" : "student"}

#copying dictionary a 
x = a.copy()
print(a)

#returning value of a specified key 
x = a.get("age")
print(x)

#setdefault()
x = a.setdefault("name", "address")
print(x)

#returning list containing dict keys 
x = a.keys()
print(x)

#returning list of all values in dict 
x = a.values()
print(x)

#removing element with specified key 
a.pop("occupation")
print(a)

#returning list containing tuple for each key-value pair 
x = a.items()
print(x)

#removing last inserted key-value pair 
a.popitem()
print(a)

#updating dict with specified key-value pairs 
a.update({"nationality" : "Indian"})
print(a)

#returning dict with specified keys & values
x = ('r', 's', 't')
y = 1

b = dict.fromkeys(x, y)
print(b)

#removing all elements from dict a
a.clear()
print(a)
