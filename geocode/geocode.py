import json
import urllib.request, urllib.parse, urllib.error

service_url = 'http://py4e-data.dr-chuck.net/json?'

while True:
    address = input('enter address')
    if len(address) < 1: break

    url = service_url + urllib.parse.urlencode({'address': address, 'key': 42})

    print('Retrieving:', url)
    page = urllib.request.urlopen(url)
    data = page.read().decode()

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('Fail')
        continue
    print(js)
    answer = js['results'][0]['place_id']
    print(answer)