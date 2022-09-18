'''f= open("anotherfile.txt","w") # similarly u can open a file in append mode to add something at the end 
data= f.write("please write my name is sushree") # cant belive it just create a new file for me 
data= f.write("you are amazing")
print(data)
f.close()'''
#use of with statement
with open("anotherfile.txt","w") as f:
    data=f.write("me") #Here u dont need to write f.close() as its automatically done using this syntax
