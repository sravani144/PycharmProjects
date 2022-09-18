#range operator in for loop
for i in range(8):
    print(i)
for i in range(2,8):
    print(i)
for i in range(2,8,2):
    print(i)
# use for break statement
for i in range(0,9):
    print(i)
    if i==5:
        break
# use of continue statement (Used for skipping values )   
for i in range(0,8):
    if i==5:    
        continue
    print(i)
# use of pass statement (its a null statement which means do nothing)    
for i in range(0,8):
    if i<=8:
        pass #if i remove pass it will throw error
    print("cutipie")




    
    
