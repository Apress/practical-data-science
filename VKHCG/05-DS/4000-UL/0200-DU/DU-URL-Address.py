import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
http = urllib3.PoolManager()

for longitude in range(-180,180,10):
    for latitude in range(-90,90,10):
        sURL='https://maps.googleapis.com/maps/api/geocode/json?latlng=' + \
        str(latitude) + ',' + str(longitude) + '&key='
        #sURL='https://maps.googleapis.com/maps/api/geocode/json?latlng=38.908133,-77.047119&key='
        #print(sURL)
        r = http.request('GET', sURL)
        datastatus=results=json.loads(r.data.decode('utf-8'))['status']
        if datastatus=='OK':
            results=json.loads(r.data.decode('utf-8'))['results']
            result=results[0]
            geodata = dict()
            for i in range(len(result['address_components'])):
                if result['address_components'][i]['types'][0] == 'country':
                    geodata['cc'] = result['address_components'][i]['short_name']
            geodata['lat'] = result['geometry']['location']['lat']
            geodata['lng'] = result['geometry']['location']['lng']
            geodata['address'] = result['formatted_address']
            
            print('{address}. (lat, lng) = ({lat}, {lng}) Country = {cc}'.format(**geodata))