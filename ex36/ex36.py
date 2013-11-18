from sys import exit

def dark_room():
	print "You wake up in a dark room."
	print "A single light illuminates a red door"

	while True:
		next = raw_input("> ")
		test = True
		if next == "ignore" and test:
			dead("You died.")
			test = False
			

		elif next == "open" and test:
			red_room()
		else:
			print "Enter a valid command"

def red_room():
	print "Behind the red is a"
	next = raw_input("> ")









def dead(why):
	print why, ":("
	exit(0)






dark_room()
