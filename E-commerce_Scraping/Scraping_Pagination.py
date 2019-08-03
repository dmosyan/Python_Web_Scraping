import pandas as pd
import requests
from bs4 import BeautifulSoup
from openpyxl.workbook import Workbook

link = "http://webscraperio.us-east-1.elasticbeanstalk.com/test-sites/e-commerce/static/computers/tablets?page="
products = []

for page in range(1, 5):
    webpage = requests.get(link + str(page))
    content = webpage.content
    result = BeautifulSoup(content, 'html.parser')
    products_on_page = result.find_all("div", {"class": "col-sm-4 col-lg-4 col-md-4"})

    for product in products_on_page:
        products.append(product)

print(len(products)) #Result is: 21

names = []
links = []
prices = []

for item in products:
    names.append(item.a.string)
    links.append("https://www.webscraper.io" + item.a['href'])
    prices.append(item.h4.string)

data = list(zip(names,links,prices))

df = pd.DataFrame(data, columns = ['Name', 'Link', 'Prices'])
df.to_excel("C:\\Users\David\\Desktop\\Python_WebScraping\\Course\\E-commerce_Scraping\\Scraping_pagination.xlsx")

#END