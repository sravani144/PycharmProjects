class employee: #parent class
    company="Google"
def showdetails(self):
    print("this is an employee")    

class programmer (employee):# here we have a child class programmer which is inherited from parent class employee
    # def showdetails(self): 1st preference will be object inherited within child class if it is unable to find a object here it will look for the parent class
        print("this is a programmer")
e= employee()
p= programmer()    
s= e.showdetails("self")   

