fr = float(input("Enter a frequency (Hz): "))
name = ""
if fr == 261.63:
    name= "C4"
elif fr == 293.66:
    name = "D4"
elif fr == 329.63:
    name = "E4"
elif fr == 349.23:
    name = "F4"
elif fr == 392.00:
    name = "G4"
elif fr == 440.00:
    name = "A4"
elif fr == 493.88:
    name = "B4"
if name == "":
    print('Frequency does not correspond to any musical note')
else:
    print("Frequency", fr, "corresponds to musical notes", name)


