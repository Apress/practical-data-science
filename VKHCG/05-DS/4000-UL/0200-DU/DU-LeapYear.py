import datetime
for year in range(1960,2025):
    month=2
    day=29
    hour=0
    correctDate = None
    try:
        newDate = datetime.datetime(year=year,month=month,day=day,hour=hour)
        correctDate = True
    except ValueError:
        correctDate = False
        
    if correctDate == True:
        if year%400 == 0: 
            print(year, 'Leap Year (400)')
        else:            
            print(year, 'Leap Year')
    else:
        print(year,'Non Leap Year')