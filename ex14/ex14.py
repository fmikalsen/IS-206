from sys import argv

script, user_name = argv
arw = "> "

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(arw)

print "Where do you live %s?" % user_name
lives = raw_input(arw)

print "What kind of computer do you have?"
computer = raw_input(arw)

print """
You stated %r when I asked if you liked me.
You live in %r.
And you have a %r computer
""" % (likes, lives, computer)