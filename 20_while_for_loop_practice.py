#multiplication table using while loop
num=int(input("enter a num"))
i=1
while(i<=10):
    print(num,"*",i,"=",num*i)# here strings and int is concatenated using ,
    i=i+1 
#multiplication table using for loop
num=int(input("Enter a number"))
for i in range(1,11):
    print(f"{num}*{i}={num*i}") # here I have used f strings(f in start of a string) to make things more simple
#=================================
l1=["sonali","Kajal","somali","Gunjan"] 
for names in l1:
    if names.startswith("s"):
        print("Hello"+names)
#=================================
# a number is prime if its divisible by 1 and the number itself
num=int(input("enter a number"))
for i in range(2,num):
    if (num%i ==0):
        print("number is not prime") 
        break
    else:
        print("number is prime")
#========================================
#sum of 1st n natural numbers
from math import factorial


num=int(input("enter a number"))
sum=0
for i in range(0,num+1):
    sum= (num*(num+1))//2
    print(sum)
#========================================
num=int(input("enter a number"))
factorial=1
for i in range(1,num+1):
    factorial=factorial*i
    print(factorial)
#========================================
#print star pattern
n=4
for i in range(4):
    print("*" * i)
#=======================================
n=4
for i in range(4):
    print("*" * (n-i))
#=======================================
n=3
for i in range(3):
    print("  " * (n-i-1),end=" ")
    print("*" * (2*i+1), end= " ")
    print("  " * (n-i-1))
#==========================================
#Multiplication table using reverse order 
num=int(input("Enter a number"))
for i in range(10,0,-1):
    print(f"{num}*{i}={num*i}")
         


       