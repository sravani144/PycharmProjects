def percent(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3]/400)*100)
    return p
marks1=[40,80,50,20]
percentage1=percent(marks1)    
marks2=[48,80,64,50]
percentage2=percent(marks2)
print(percentage1,percentage2)
#=====================================
#greet a user 
def greet(name):
    print("Good morning" + name)
greet("sush")
#=======================================
#default parameter value
def greet(name="stranger"):
    print("Good morning" + name)
greet("sush")
greet() #here in function call the name is empty()
#==========================================
#some mathematical operations using functions
def mysum(num1,num2):
    s=num1+num2
    return s
s= mysum(30,20)  
print(s)
#========================================
def maximum(num1,num2,num3):
    if(num1>num2 and num1>num3):
        return num1
    elif(num2>num1 and num2>num3):
        return num2
    else:
        return num3
m= maximum(4,5,8) 
print(m)               
