letter = '''Dear<|name|>
you are selected
<|date|>'''
name= input("enter your name")
date= input("enter date")
letter= letter.replace("|name|", name)
letter= letter.replace("|date|", date) 
print(letter)
