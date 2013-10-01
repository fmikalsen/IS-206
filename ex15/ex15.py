from sys import argv

script, = argv #requires full path ex. "ex15/test.txt"

#opens the file specified in the argument
#by using the open method and giving
#the open method a variable named txt


filename = raw_input("File: ")
txt = open(filename) #requires full path ex. "ex15/test.txt"
print "Heres your file %r" % filename
print txt.read() #this line will read the opened file

# print "Type filename again:"
# file_again = raw_input("> ") #requires full path ex. "ex15/test.txt"

# txt_again = open(file_again)
# print txt_again.read()