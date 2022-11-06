'''mydict={
    "kursi" : "chair",
    "pankha" : "fan",
    "kitab" : "book"
}
a=input("enter a hindi word\n")
print(mydict[a])'''
#===============================================
'''num1= int(input('enter num1\n'))
num2= int(input('enter num2\n'))
num3= int(input('enter num3\n'))
num4= int(input('enter num4\n'))
s= {num1,num2,num3,num4}
print(s)'''
# ===================================================
'''s = {18, "18", 18.1} # set always prints unique values, so it will get printed w/o any errors 
print(s)'''
# ===================================================
'''s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))'''
# ======================
mydict= {"number":[1,2], "cap": "Topi"} #one key can contain mutiple values but in form of list
mydict["number"].append(3) #you can add more values by using the append function
print(mydict)