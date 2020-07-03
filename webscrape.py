from urllib.request import urlopen as web_client
from bs4 import BeautifulSoup as soup
import re

url = "https://www.newegg.com/Headphones/Category/ID-158?Tid=167717"

uClient = web_client(url)
webpage_html = uClient.read()
uClient.close()

page_soup = soup(webpage_html, "html.parser")

divs = page_soup.findAll("div", {"class":"item-container"})

filename = "headphones.csv"
f=open(filename, "w")

headers = "title, price\n"

f.write(headers)

#Searches through each product listing
for div in divs:
    title = div.a.img["title"]
    #Finds price div in HTML and removes unnecessary tags
    price_div = div.find("li", {"class":"price-current"})
    dollars = re.sub('[^0-9]', '', str(price_div.strong))
    cents = re.sub('[^0-9]', '', str(price_div.sup))
    total_price = dollars + "." + cents
    
    print("Title: " + title)
    print("Price: " + total_price)

    f.write(title.replace(",", "|") + "," + total_price + "\n")

f.close()
