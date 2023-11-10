name = input("Enter the name of a note:")
letter = name[0] 
octave = int(name[1])  
fr = 0
if letter == "C":
    fr = 261.63
elif letter == "D":
    fr = 293.66
elif letter == "E":
    fr = 329.63
elif letter == "F":
    fr = 349.23
elif letter == "G":
    fr = 392.00
elif letter == "A":
    fr = 440.00
elif letter == "B":
    fr = 493.88
if fr == 0:
    print("No frequency found for musical note", name)    
else:   
    fr /= 2 ** (4 - octave)  
    print("The frequency of", name, "is", fr, "Hz")




