################################################################
# -*- coding: utf-8 -*-
################################################################
import os
import sys
from datetime import datetime
from pytz import timezone, all_timezones

################################################################
if sys.platform == 'linux': 
    Base=os.path.expanduser('~') + '/VKHCG'
else:
    Base='C:/VKHCG'
################################################################
print('################################')
print('Working Base :',Base, ' using ', sys.platform)
print('################################')
################################################################
sFileDir=Base + '/01-Vermeulen/01-Retrieve/01-EDS/02-Python'
if not os.path.exists(sFileDir):
    os.makedirs(sFileDir)
################################################################
sFileName=sFileDir + '/Retrieve-TimeZones.csv'
f = open(sFileName, 'w')
for zone in all_timezones:
    print(zone)
    sLine=zone + '\n'
    f.write(sLine)
f.close()
################################################################
now_date = datetime.now()
print('Local Date Time:',str(now_date.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))
now_utc=now_date.replace(tzinfo=timezone('UTC'))
print('UTC Date Time:',str(now_utc.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))

now_date_local=datetime.now()

#Change the localtime to 'Europe/London' local time by tagging it as 'Europe/London' time.

now_date=now_date_local.replace(tzinfo=timezone('Europe/London'))

print('London Date Time:',str(now_date.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))

#Now you have a time zone enabled data time value you can use to calculate other timezones.
#First convertion you perform is to the UTC time zone:

now_utc=now_date.astimezone(timezone('UTC')) 
print('UTC Date Time:',str(now_utc.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))

#What is the time in London, UK?
 
now_eu_london=now_date.astimezone(timezone('Europe/London')) 
print('London Date Time:',str(now_eu_london.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))

#What is the time in Berlin, Germany?

now_eu_berlin=now_date.astimezone(timezone('Europe/Berlin')) 
print('Berlin Date Time:',str(now_eu_berlin.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))

#What is the time in Jersey Islands, UK?
 
now_eu_jersey=now_date.astimezone(timezone('Europe/Jersey')) 
print('Jersey Date Time:',str(now_eu_jersey.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))

#What is the time in New York, USA?

now_us_eastern=now_date.astimezone(timezone('US/Eastern')) 
print('USA Easten Date Time:',str(now_us_eastern.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))

#What is the time in Arizona, USA?


now_arizona=now_date.astimezone(timezone('US/Arizona')) 
print('USA Arizona Date Time:',str(now_arizona.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))

#What is the time in Auckland, Australia?

now_auckland=now_date.astimezone(timezone('Pacific/Auckland')) 
print('Auckland Date Time:',str(now_auckland.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))

#What is the time in Yukon, Canada?

now_yukon=now_date.astimezone(timezone('Canada/Yukon')) 
print('Canada Yukon Date Time:',str(now_yukon.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))

#What is the time in Reykjavik, Iceland?

now_reyk=now_date.astimezone(timezone('Atlantic/Reykjavik')) 
print('Reykjavik Date Time:',str(now_reyk.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))

#What is the time in Mumbai, India?

now_india=now_date.astimezone(timezone('Etc/GMT-7')) 
print('India Date Time:',str(now_india.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))



#What time zones does Vermeulen use?

print('Vermeulen Companies') 
print('Local Date Time:',str(now_date_local.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))
print('HQ Edinburgh:',str(now_utc.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)"))) 
print('Iceland Thor Computers:',str(now_reyk.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)"))) 
print('USA Arizona Computers:',str(now_arizona.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))

#Next is Krennwallner?
print('Krennwallner Companies') 
print('Local Date Time:',str(now_date_local.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))
print('HQ Berlin:',str(now_eu_berlin.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)"))) 
print('HQ USA:',str(now_us_eastern.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))


#What about Hillman:
print('Hillman Companies')
print('HQ London:',str(now_eu_london.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)"))) 
print('HQ USA:',str(now_arizona.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)"))) 
print('HQ Canada:',str(now_yukon.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))
print('HQ Australia:',str(now_auckland.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)"))) 
print('HQ India:',str(now_india.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)"))) 


#Just Clark to look at:

print('Clark Companies') 
print('HQ Jersey:',str(now_eu_jersey.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))
print('HQ Berlin:',str(now_eu_berlin.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)"))) 
print('HQ USA:',str(now_us_eastern.strftime("%Y-%m-%d %H:%M:%S (%Z) (%z)")))
