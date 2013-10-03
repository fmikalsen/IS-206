
def test(x, y):
	return x * y

m1 = float(raw_input("First number: "))
m2 = float(raw_input("Second number: "))
result = test(m1, m2)	
	
print "Result: %.1f" % result