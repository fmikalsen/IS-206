myName = "Frode Mikalsen"
myAge = 25
myHeight = 176#Centimetres
myWeight = 93 #Kilograms
myEyes = "Grey"
myTeeth = "White"
myHair = "Dark brown"
kgToLbs = myWeight * 2.2

print "Let's talk about %s." % myName
print "He's %d cm tall." % myHeight
#using %g to get the floating point decimal on the calculated pounds
print "He's about %d kg or %g lbs heavy." %(myWeight, kgToLbs)
print "He's got %s eyes and %s hair." %(myEyes, myHair)
print "His teeth are usually %s depending on the amount of coffee and/or snus." % myTeeth

#This line makes no sense at all. It just adds up the number variables.
print "If I add %r, %d, and %d I get %d." % (myAge, myHeight, myWeight, myAge + myHeight + myWeight)
