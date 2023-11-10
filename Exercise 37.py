s = int(input("Number of sides: "))
if (s == 3):
    print("Triangle")
elif (s == 4):
    print("Square")
elif (s == 5):
    print ("Pentagon")
elif (s == 6):
    print ("Hexagon")
elif (s == 7):
    print ("Heptagon")
elif (s == 8):
    print ("Octagon")
elif (s == 9):
    print ("Nonatagon")
elif (s == 10):
    print ("Decagon")
else:
    print("Error: Number of sides is not between 3 and 10")