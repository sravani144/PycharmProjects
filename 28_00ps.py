'''class employee: #here employee is a class
    company= "Google" #company is attribute
Sushree= employee()   #sushree is object (object instansation)
Sumit= employee()
print(Sushree.company)
employee.company= "microsoft" # here we have changed the company name
print(Sushree.company)'''
#================================================
# Instance attribute has more preferece/ 1st preference over class attributes
'''class employee: 
    company= "Google"
    salary= 500
Sushree= employee()   
Sumit= employee()
Sushree.salary= 400
print(Sushree.company)
print(Sushree.salary) # it will take the salary/give 1st preference to instance attribute
print(Sumit.salary)''' # but for sumit we do not have instance attribute for slary henec it will consider the salary from class attribute
#===========================================
#self method
'''class employee:
    company= "Amazon"
    salary= 400
    def get_salary(self): # here self refers to sushree
     print(f"salary of employee is{self.salary}")
sushree= employee()     
sushree.get_salary()'''
#==============================================
# Static method
'''@ staticmethod
def greet():
    print("Good morning")'''
#===========================================
    

