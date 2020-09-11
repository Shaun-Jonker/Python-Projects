import json
import urllib.request, urllib.parse, urllib.error

example_data = 'http://py4e-data.dr-chuck.net/comments_42.json'
actual_data = 'http://py4e-data.dr-chuck.net/comments_760918.json'

web_page = urllib.request.urlopen(actual_data)
data = web_page.read().decode()

print('Retrieved:', len(data), 'Characters')

js = json.loads(data)

total = 0

for comment in js['comments']:
    num = comment['count']
    total += int(num)

print(total)