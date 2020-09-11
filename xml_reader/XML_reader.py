import urllib.request
import xml.etree.ElementTree as ET

url = input("Input Url")
xml = urllib.request.urlopen(url).read()

total = 0

tree = ET.fromstring(xml)
lst = tree.findall("comments/comment")

for item in lst:
    num = item.find('count').text
    total += int(num)

print(total)
