# l1= [10,20,30,"payal", 0.6,"tiki"]
# print(l1)
# l1[3]= "benu"
# print(l1)
l2= [44,5,18,7,20]
l3= l2.copy() # using copy operation we can copy the entire l2 list into l3
# l2.sort() # arranges the data in acending order
# print(l2)
# l2.append(46) #adds the value at end
# l2.reverse() it reverses the list
# l2.insert(2,3) adds the data based on index position 2 is index vale
# l2.remove(7) removes the particular value
#l2.pop(2) removes value based on index position but ny default it will remove the last data
l3.extend([2,3]) #extend operation is used to insert a small list into existing list 
l3.append([2,3]) # just see the diff here [2,3] is added as it is
print(l3)
