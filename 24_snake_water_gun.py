from random import randint, random


def gamein(comp,player):
    if comp==player:
        return None
    elif comp=="s":
        if player=="w":
            return False
        elif player=="g":
            return True      
    elif comp== "w":
        if player=="s":
            return True
        elif player=="g":
            return True
    elif comp== "g":
        if player=="s":
            return False
        elif player=="w":
            return True
print("comp turn : snake(s) water(w) gun(g)?")    
randnum= randint(1,3)  
if randnum==1:
    comp= "s"
elif randnum==2:
    comp= "w"
elif randnum==3:
    comp= "g"
you= input("your turn : snake(s) water(w) gun(g)?")     
game=gamein(comp,you)  
#print(f"com chose{comp}")
#print(f"you chose{you}")
if game==None:
    print("this is a tie")
elif game:
    print("you win")
else:
    print("you loose")    





