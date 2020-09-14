from selenium import webdriver
import csv
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--disable-gpu")
# chrome_options.add_argument("--no-sandbox") # linux only
chrome_options.add_argument("--headless")

evetech = webdriver.Chrome(options=chrome_options)


evetech.get("https://www.evetech.co.za/PC-Components/buy-solid-state-drives-83.aspx")
print('=====Running Evetech in headless mode=====')

eve_product_names = [name.text for name in evetech.find_elements_by_class_name('myProductName')]
eve_prices = [price.text for price in evetech.find_elements_by_class_name('price')]
eve_status = [s.text for s in evetech.find_elements_by_class_name('statuslbl_In')]
eve_links = [link.get_attribute('href') for link in evetech.find_elements_by_link_text('More Info')]

print("=====Finished Evetech Collection=====")
print('=========Now writing to file=========')

products = sorted(zip(eve_product_names, eve_prices, eve_status, eve_links))


with open('SSD.csv', "w", newline='') as the_file:
    csv.register_dialect("custom", delimiter=",")
    writer = csv.writer(the_file, dialect="custom")
    for item in products:
        writer.writerow(item)
print("=====Writing to file complete=====")

wootware = webdriver.Chrome(options=chrome_options)

wootware.get("https://www.wootware.co.za/computer-hardware/hard-drives-ssds/solid-state-disks/shopby"
             "/in_stock_with_wootware?limit=500")

print('=====Running Wootware in headless mode=====')

woot_name = [n.text for n in wootware.find_elements_by_class_name('product-name')]
woot_price = [p.text for p in wootware.find_elements_by_class_name('price')]
woot_saving = [s.text for s in wootware.find_elements_by_class_name('special-price-saving')]
woot_elems = wootware.find_elements_by_css_selector(".products-grid .product-name a")
woot_links = [elem.get_attribute('href') for elem in woot_elems]

print("=====Finished Wootware Collection=====")
print('==========Now writing to file=========')

woot_products = sorted(zip(woot_name, woot_price, woot_saving, woot_links))

with open('SSD.csv', "a+", newline='') as the_file:
    csv.register_dialect("custom", delimiter=",")
    writer = csv.writer(the_file, dialect="custom")
    for item in woot_products:
        writer.writerow(item)


evetech.close()
wootware.close()

