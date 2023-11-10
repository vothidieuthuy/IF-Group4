month=input('Enter the name of a month:')
days=31
if month == 'February':
    days = 28 or 29
elif (month=='April') or (month=='June') or (month=='September') or (month=='November'):
    days=30
print(month,'has',days,'days')