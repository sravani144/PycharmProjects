#prevent printing of print() in new line
'''print("hello",end=" ")
print("How",end=" ")
print("are",end=" ")
print("you")'''
#==================================
#factorial using recursion: logic (n-1)!*n
'''def factorial_recursion(n):
        if n==0 or n==1:
            return 1
        else:
            return (factorial_recursion(n-1)*n)
f= factorial_recursion(4)
print(f)'''
#====================================
#sum of n natural numbers using recursion : sum(n-1)+n
'''def sum_recursion(n):
    if n==0 or n==1:
        return 1
    else:
        return sum_recursion(n-1)+n
s= sum_recursion(5)
print(s)'''        
#====================================
# Remove a word from string and strip it at the same time
# strip is used to remove white spaces from a string
'''str= ("    Sush is good girl     ")    
print(str)
print(str.strip())'''
#========================================
'''def remove_and_strip(string, word):
    newstr = string.replace(word,"")
    return newstr.strip()
str= "sush is a good girl"    
s= remove_and_strip(str,"a")
print(s)'''
#==========================================

                        


