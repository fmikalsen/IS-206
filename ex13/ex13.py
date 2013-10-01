from sys import argv

#This require the user to pass 2 arguments
#when running the script
script, arg1, arg2 = argv 

print "The script is called", script
x = raw_input("Please pass another variable: ")

print "First variable is %r and the second is %r \n the third is %r" % (
arg1, x, arg2)
