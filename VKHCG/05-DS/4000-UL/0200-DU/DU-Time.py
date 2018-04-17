from datetime import datetime
from pytz import timezone , all_timezones
now_date = datetime(2001,2,3,4,5,6,7)
now_date = datetime.now()
now_utc=now_date.replace(tzinfo=timezone('UTC'))
print('Date:',str(now_date.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))
print('Date:',str(now_utc.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))
print('Year:',str(now_utc.strftime("%Y")))
print('MonthName:',str(now_utc.strftime("%B")))
print('Month:',str(now_utc.strftime("%m")))
print('Day:',str(now_utc.strftime("%d")))
print('Hour:',str(now_utc.strftime("%H")))
print('Minute:',str(now_utc.strftime("%M")))
print('Second:',str(now_utc.strftime("%S")))
print('milliSecond:',str(now_utc.strftime("%f")))
print('weekday:',str(now_utc.strftime("%w")))
print('week of year:',str(now_utc.strftime("%YW%WD%w")))
print('Day of year:',str(now_utc.strftime("%Y/%j")))

print('Zones:',len(all_timezones))
#for zone in all_timezones:
#    print(zone)