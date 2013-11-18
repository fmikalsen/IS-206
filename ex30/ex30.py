people = 70
cars = 50
buses = 50

if cars > people:
	print "\tWe should take the cars"
elif cars < people:
	print "\tWe should not take the cars"
else:
	print "\tWe can't decide"

if buses > cars:
	print "\tThat's too many buses"
elif buses < cars:
	print "\tMaybe we could take the buses"
else:
	print "\tWe still can't decide"

if people > buses:
	print "\tAlright, lets just take the buses"
else:
	print "\tFine lets stay home then"

#custom example
if people < cars and cars > buses:
	print "CAR!"
elif people < buses and buses > cars:
	print "BUS!"
elif people >= cars and people >= buses:
	print "There are too many people!"
else:
	print "Same amount of cars and buses"
#if, elif and else is the same as if elseif en else in java
