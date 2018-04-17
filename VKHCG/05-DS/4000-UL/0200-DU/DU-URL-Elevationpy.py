import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()

for longitude in range(-180,180,10):
    for latitude in range(-90,90,10):
        sURL='https://maps.googleapis.com/maps/api/elevation/json?locations=' + \
        str(latitude) + ',' + str(longitude) + '&key='         
        #sURL='https://maps.googleapis.com/maps/api/elevation/json?locations=38.908133,-77.047119&key='
        #print(sURL)
        r = http.request('GET', sURL)
        datastatus=results=json.loads(r.data.decode('utf-8'))['status']
        if datastatus=='OK':
            results=json.loads(r.data.decode('utf-8'))['results']
            result=results[0]
            print('Latitude',result['location']['lat'])
            print('Longitude',result['location']['lng'])
            print('Elevation',result['elevation'])
    