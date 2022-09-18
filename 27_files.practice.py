'''f= open("poem.txt","r")
t= f.read()
if "twinkle" in t:
    print("yes")
else:
    print("no")    
f.close()'''
# ===========================================
'''for i in range(1,21):
    with open(f"multiplication_table_of_{i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}\n")
            break'''
#================================================
from dataclasses import replace


'''with open("sample.txt","r") as f:
    content= f.read()
    content= content.replace("donkey"," ")    
with open("sample.txt","w") as f:
    f.write(content)'''        
#============================================
contents= ["donkey","Fool","stupid","good"]
with open("contents.txt","w") as f:
    for words in contents:
        contents= contents.replace("donkey","###")
        contents= contents.replace("Fool","###")
        contents= contents.replace("stupid","###")
f.write(contents)        
#===========================================

        
