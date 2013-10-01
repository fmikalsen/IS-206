print "What is your nickname?",
nick = raw_input()

#this is another option to do it
game = raw_input("What game do you play the most? ")

print "Are you any good? 1-10 - 10 beeing awesome",
skill = int(raw_input())

print "So, you're nickname is %r, you play %r and your skill level is %r"% (
nick, game, skill
)