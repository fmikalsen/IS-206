def loop(numbers, i, x, z):

	while i < x:
		print "At the top i is %d" % i
		numbers.append(i)

		i += z
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num
	
i = 0
x = 11
z = 2
numbers = []

loop(numbers, i, x, z)
