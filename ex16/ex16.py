 from sys import argv

script, filename = argv

print "We're goint to erase %r" % filename
print "If you don't want that, hit CTRL-C."
print "If this sounds good, press ENTER."

raw_input("?")

print "Opening the file..."
target = open(filename, "w")


#truncating the file was not necessary since we use the "w" parameter
#
#print "Truncating the file. cya!"
#target.truncate()

print "Not I'm gonna ask you for three lines."

line1 = raw_input("First line: ")
line2 = raw_input("Second line: ")
line3 = raw_input("Third line: ")

text = "%s \n%s \n%s" % (line1, line2, line3)

target.write(text)

target.close()
print "And finally, we close it."
