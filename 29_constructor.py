'''class programmer:
    comapany= "Microsoft"

    def __init__(self,name,product): #constructor syntax which has arguments within braces
        self.name= name
        self.product= product
    def getinfo(self):    
       print(f"the name of pragrammer is {self.name} and product is {self.product}") 

harry = programmer("Harry","skype")
harry.getinfo()'''
# ==============================================
class calculator():
    def __init__(self,num):
        self.number= num
    def square(self):    
     print(f"the square of number{self.number} is {self.number}**2 ")    
    def squarert(self):
        print(f"the squarert of {self.number}is {self.number}**0.5")    
    def cube(self):
        print(f"the cube of number {self.number}is {self.number}**3")
a= calculator(9) # after writing the logic you need to do object instatiation    
a.cube()
a.square()
a.squarert()      
