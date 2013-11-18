from sys import exit
import random

class Scene(object):

	def enter(self):
		print "Not configured"
		pass

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n----------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
	quips = [
        "you dead!",
         "Oh shit, you died",
         "Geez, get on my level, hoe!",
         "Yup, you just lost your life"
	]

	def enter(self):
		print Death.quips[random.randint(0, len(self.quips)-1)]
		exit(1)

class DarkRoom(Scene):

	def enter(self):

		print "You wake up in a dark room."
		print "The last thing you remember is that"
		print "you where walking home from a party late at night"
		print "\nInfront of you there's a gift wrapped box saying: Open me!"
		print "Do you want to open the box?"

		action = raw_input("> ")
		
		if action == "yes":
			print "you open up the box."
			print "Inside you find a drawing of a dragon, singing"
			print "Weird!"
			return "door"

		elif action == "no":
			print "you completely ignore the gift wrapped box"
			return "door"

		elif action == "mellon":
			print "Oh shit! All those hours watching LOTR finally paid off!"
			return "finish"
			
		else:
			print "wtf do you mean? try again"
			return "dark_room"

class Door(Scene):
	
	def enter(self):
		print "Oh shit! you just found a door in the dark room."
		print "Damnit, theres a combination lock!"
		print "So, uhm.. yeah, crack the code."
		print "It looks like its a 3 digits combination with numbers from 1-3"
		
		code = "%d%d%d" % (random.randint(1,3), random.randint(1,3), random.randint(1,3))
		guess = raw_input("> ")
		tries = 1		

		while guess != code and tries < 20:
			print "Wrong code, bro try again!"
			tries += 1
			guess = raw_input("> ")

		if guess == code:
			print "WHAAAT! You did it! Good job dude"
			print "You open the door and enter inside"
			return "item_room"

		else:
			print "The door just exploded in your face!"
			return "death"
		

class ItemRoom(Scene):
	item_selected = ""
	#get the fucking karaoke machine to defeat the dragon

	def enter(self):
		
		print "Aight, you just entered a completely white room."
		print "On the middle of the room theres a table and on it theres 3 items"
		print "Since you don't make the rules you can only carry 1 item with you"
		print "What do you take?"
		print "1 = Giant ass sword"
		print "2 = Karaoke machine, wtf?!"
		print "3 = Steven Segal's pony tail"

		item = raw_input("> ")
		
		if item == "1":
			print "You selected the sword, it's fucking heavy."
			print "With the sword on your back you continue to the next room"
			ItemRoom.item_selected = "1"
			return "singing_dragon"

		elif item == "2":
			print "You chose the karaoke machine"
			print "and continue to the next room"
			ItemRoom.item_selected = "2"
			return "singing_dragon"

		elif item == "3":
			print "Ok, you continue your journey with a lock of hair."
			print "Great decision making..."
			ItemRoom.item_selected = "3"
			return "singing_dragon"

		else:
			print "wtf do you mean? try again"
			return "item_room"

class SingingDragon(Scene):

	def enter(self):
		print "Nothing much to see in this room."
		print "Except the MASSIVE FIRE BREATHING RED DRAGON!!!"
		print "It looks like it's guarding Natalie Portman, you must save her!"
		print "WTF do you do?"

		decision = raw_input("> ")

		if decision == "go back":
			print "you turn around and go back to the previous room"
			return "item_room"

		elif decision == "use item":

			item_to_use = ItemRoom.item_selected
			
			if item_to_use == "1":
				print "You charge the dragon with the sword!"
				print "The dragon scales are too hard and you dont"
				print "do any damage at all."
				print "The dragon incinerate you with its breath"
				return "death"

			elif item_to_use == "2":
				print "You put down the karaoke machine and press play."
				print "Instantly the dragon stops beeing scary and yell:"
				print "'Oh snap! Thats my jam!' and starts singing"
				print "While the dragon sings you save Natalie Portman."
				return "finish"

			elif item_to_use == "3":
				print "You stand still with the god damn pony tail in"
				print "your hand, looking stupid as fuck."
				print "The dragon laughs at you and stomps you to death"
				return "death"

		elif decision == "fight":
			print "Yeah, good idea. Fight a dragon."
			return "death"

		elif decision == "flee":
			print "You try to flee but the dragon hurls a fireball at you."
			print "You died while looking lika a pussy who runs away."
			return "death"

		else:
			print "wtf do you mean? try again"
			return "singing_dragon"

class Finished(object):

	def enter(self):
		print "You just finished the fucking game"
		print "You and Natalie Portman live happily together forever!"
		print "Congrats bro"
		exit(1)
	


class Map(object):

	scenes = {
		"dark_room": DarkRoom(),
		"item_room": ItemRoom(),
		"singing_dragon": SingingDragon(),
		"door": Door(),
		"death": Death(),
		"finish": Finished()
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map("dark_room")
a_game = Engine(a_map)
a_game.play()










