from sys import exit
import random
from rooms import *

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()

		while True:
			print "\n----------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

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










