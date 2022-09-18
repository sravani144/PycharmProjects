'''st="this is a string with double    space"
st= st.replace("  ", " ")
st= st.find("  ")
print(st)'''
#===============Check if a string is symmetrical/pallindrome==========================
'''str= input("enter a string\n")
mid= int(len(str)//2)
if str[:mid]== str[mid:]:
    print("string is symmetrical")
else:
    print("string is not symmetrical")  
if list(str)== reversed(list(str)):# if str[:len(str)]== str[::-1] 
    print("string is pallindrome")
else:
    print("string is not pallindrome")''' 

#===========Reverse a string==========================     
'''str= input("enter a string\n")
reverse_str= str[::-1]
print(reverse_str)'''
#=================Capitalize 1st charac and  last charac of a string=========================
'''str=input("enter a string\n")
a= str.split() # we have converted sting to list using split function
res=[]
for i in a:
    b= i[0].upper()+i[1:-1]+i[-1].upper() #logic
    res.append(b) # after this we have apended it into the list 
res= "".join(res)   #now its joined back to the string
print(res)'''
# ======================y 



