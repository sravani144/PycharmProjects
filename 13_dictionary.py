mydict= {
"Sushree" : "good in maths" ,
"varsha" : "good in drawing",
"Aditya" : "good in sports"
}
'''print(mydict["Sushree"])
print(mydict["Aditya"])
print(mydict["varsha"])
# Dictionary methods'''
'''print(mydict.keys()) #print keys
print(mydict.values()) #print values
print(mydict.items()) #print both keys and values
print(type(mydict)) #specifies type of mydict'''
#print(mydict.get("Sushree")) # this is the best way to access a key in dict to get values without any error
# print(mydict.pop("Sushree")) # it will remove the particular key and its value
# print(mydict.popitem()) # it will randomly remove the key and its values
'''updatedict = {
"sumit" : "loves gym"    
}
mydict.update(updatedict)'''
print(mydict)