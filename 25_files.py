# f= open ("sample.txt","r")# this format is used to open a file in read/write mode
f= open ("sample.txt","r")
# data= f.read() # read() is a function used to read the content of a file
# data= f.read(5) #this will read 5 characters of the file and there cannot be 2 read fuction for same file post editing it
data= f.readline() # readline is used to read the 1st line
print(data)

data= f.readline() # here it will read teh 2nd line (u can write readline multiple times to read multiple lines)
print(data)
f.close() # its imp to close a file you have opened