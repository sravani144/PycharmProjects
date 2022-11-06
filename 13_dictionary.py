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
updatedict = {
"sumit" : "loves gym"    
}
mydict.update(updatedict)
print(mydict)