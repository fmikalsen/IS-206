from sys import argv

script, barg, parg = argv

def fast_food(burger, pizza):
	print "In the last month you have eaten: "
	print "%d Burgers \n%d Pizzas\n" % (burger, pizza)
	
print "Directly:"
fast_food(10, 13)

print "From arg:"
barg, parg = int(barg), int(parg) #converts argument string to integer
fast_food(barg, parg)

print "Correct the argument:"
in_b = int(raw_input("Burgers: "))
in_p = int(raw_input("Pizzas: "))
fast_food(in_b, in_p)