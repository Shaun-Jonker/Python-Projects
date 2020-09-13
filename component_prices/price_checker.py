import urllib.request, urllib.error
from bs4 import BeautifulSoup

evetech_url = 'https://www.evetech.co.za'
wootware_url = 'https://www.wootware.co.za/computer-hardware/hard-drives-ssds/solid-state-disks'
takealot_url = 'https://www.takealot.com'
my_website = 'https://www.shaunjonker.com'
try:
    # takealot_html = urllib.request.urlopen(takealot_url).read()
    # wootware_html = urllib.request.urlopen(wootware_url).read()
    # evetech_html = urllib.request.urlopen(evetech_url).read()
    my_website_html = urllib.request.urlopen(my_website).read()
except:
    print("Fetch Failed")
    quit()

# eve_soup = BeautifulSoup(evetech_html, 'html.parser')
# woot_soup = BeautifulSoup(wootware_html, 'html.parser')
# take_soup = BeautifulSoup(takealot_html, 'html.parser')
my_soup = BeautifulSoup(my_website_html, 'html.parser')

print(my_soup)