from urllib.request import urlopen as web_client
from bs4 import BeautifulSoup as soup
import re
import numpy as np

filename = "headphones.csv"
f=open(filename, "w")

headers = "title, price\n"
f.write(headers)

pages = np.arange(1, 10, 1)
for page in pages:
    url = "https://www.newegg.com/p/pl?Submit=StoreIM&Depa=10&Category=158&Page=" + str(page) + "&PageSize=96"

    uClient = web_client(url)
    webpage_html = uClient.read()
    uClient.close()

    page_soup = soup(webpage_html, "html.parser")

    divs = page_soup.findAll("div", {"class":"item-container"})
    print(len(divs))

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
