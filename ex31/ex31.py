print "you enter a dark room with two doors, wich one do you want to enter?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear inside, eating a carrot cake. What now?"
	print "1. Steal the cake"
	print "2. Scream at the bear"

	bear = raw_input("> ")

	if bear == "1":
		print "the bear eats your face off. good job!"
	elif bear == "2":
		print "the bear laugh you and rips you open. good job!"
	else:
		print "Good choice. You and the bear shares the cake :D :D :D :D"

elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina."
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello.  Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck.  Good job!"

elif door == "mellon":
	print "You found a secret door!"
	print "1. Enter"
	print "2. Ignore"

	secret = raw_input("> ")
	if secret == "1":
		print "The room is full of kittens and you have the best time EVER!"
	elif secret == "2":
		print "Thats the most stupid thing you can do when finding secret doors"
	else:
		print "God damn! just enter the room"
		
else:
    print "You stumble around and fall on a knife and die.  Good job!"

