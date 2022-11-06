from tkinter import CENTER, Y


story = "sushree is \t a good \n good girl"
list= ["&","%","*"]
# print(len(story))
# print(story.endswith("girl")) will return true/ false
# print(story.endswith("good"))
# print(story.count("o"))
# print(story.count("good"))
# print(story.capitalize()) it capitalizes the 1st charac of string
# print(story.find("is")) it finds the 1st word with is on teh string, even if there are 2 same words it picks the 1st one
# print(story.replace("sushree","sravani"))
#print(story.upper()) #convert entire string into uppercase
#print(story.lower()) convert entire string into lower case
#print(dir(story)) # give details about all the available operations in string 
# print(story.title()) it capitalizes the 1st letter of everword in a string
# print(story.swapcase()) it converts uppercase into lower and lowercase to upper
# print(story.isupper()) this returns a true/ false value
# print(story.islower())
#print("story".join(list))#used for joining a list into a string
'''a= "python"
b= "\n".join(a)
print(b)
print(a.center(20)) # here word python is printed in middle/ center of 20 characters
print(a.zfill(10)) #python has 6 charac but we have given a length of 10 , hence the remaining charac are padded with 0's towards left
'''
x= "   python   "
# print(x.strip()) strip function is used to remove unwanted space/charac/word from left or right of a string
y= "PYTHON"
#print(y.strip("P").strip("N")) it removed 1st and last charac 
# print(y.strip("T")) it wont work if you try for some other charac in middle
print(x.index("n")) #gives the index value of n in x string









9
