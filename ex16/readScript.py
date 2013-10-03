from sys import argv

script, filename = argv

print "Let's check that file! \n"

filereader = open(filename, "r") #"r" is not necessary since it's default

print filereader.read()
print ""