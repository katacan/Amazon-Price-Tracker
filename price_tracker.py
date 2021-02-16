import requests
import bs4
import pandas as pd

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
    }

offer = []

def price_tracker(url, targetPrice) :
    res = requests.get(url, headers=header)
    soup = bs4.BeautifulSoup(res.content, features='lxml')

    try :
        title = soup.find(id="productTitle").get_text().strip()
        price = float(soup.find(id='priceblock_ourprice').get_text().replace('.', '').replace('€', '').replace(',', '.').strip())
        if price <= targetPrice:
            offer.append("The {0} is {1} now ! Check it out : {2}".format(title, price, url))

    except :
        offer.append("There is no detail about the product")

df = pd.read_csv("https://docs.google.com/spreadsheets/u/1/d/121xVxzbX1t0xYRkTWzanYrvhUUIQ2Y-xzNSoyeJbPEs/export?format=csv&id=121xVxzbX1t0xYRkTWzanYrvhUUIQ2Y-xzNSoyeJbPEs&gid=0")
for i in range(0,len(df["URL"])):
    price_tracker(df["URL"][i],df["Target Price"][i])

print(offer)