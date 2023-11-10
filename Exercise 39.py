de=float(input('Enter the number of decibels:'))	
if (de>0) and (de<40):
    print('Sound level is quieter than a quiet room')		
elif (de==40):
    print('Sound level is equivalent to a quiet room.')	
elif (de>40) and (de<70):
    print('Sound level is quieter than an alarm clock.')
elif (de==70):
    print('Sound level is equivalent to an alarm clock')		
elif (de>70) and (de<106):
    print('Sound level is quieter than a lawn mower.')	
elif (de==106):
    ('Sound level is equivalent to a lawn mower.')	
elif (de>106) and (de<130):
    print("Sound level is quieter than a jackhammer.")		
elif (de==130):
    print('Sound level is equivalent to a jackhammer.')		
elif (de>130):
    print('Sound level is way too loud.')		
else:
    print('Error number')		
