class Song(object):
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		print "-" * 10
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy birthday to you",
		   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
			"With pockets full of shells"])

cw_lyrics = ["I live between","concrete walls"]

concrete_walls = Song(cw_lyrics)

concrete_walls.sing_me_a_song()

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


