a = {1,2,3,4}
a.add(5) #adds a new number inside set 
a.add(6)
a.remove(6) #removes 6 from the set
a.add(1) # repetion is not allowed in set
'''a.add([1,8,9]) #list cannot be added inside a set as its unhashable(values can be changed)
a.add({1:7}) # dictionary cannot be added inside a set as its unhashable(values can be changed)'''
a.add((1,8,9)) # tuples can be added inside a set as its hashable(values of tuples cant be changed)
print(a)
print(len(a)) #prints the lenght of the set 
# note the diff b/w an empty set and empty dictionary
b= {} #syntax for empty dict
print(type(b))
c = set() #syntax for empty set
print(type(c))