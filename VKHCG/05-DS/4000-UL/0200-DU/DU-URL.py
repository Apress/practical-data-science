import urllib3
import json
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()

for longitude in range(-180,180,10):
    for latitude in range(-90,90,10):
        sURL='https://maps.googleapis.com/maps/api/timezone/json?location=' + \
        str(latitude) + ',' + str(longitude) + '&timestamp=1458000000&key='
        r = http.request('GET', sURL)
        datastatus=json.loads(r.data.decode('utf-8'))['status']
        
        if datastatus == 'OK':
            datatimeZoneId=json.loads(r.data.decode('utf-8'))['timeZoneId']            
            datatimeZoneName=json.loads(r.data.decode('utf-8'))['timeZoneName']
            print(datatimeZoneId,'/',datatimeZoneName)
        else:
            print(datastatus)
        time.sleep(1)
