import pandas as pd
import requests
from bs4 import BeautifulSoup
import openpyxl
from openpyxl.workbook import Workbook

#Getting the webpage
webpage = requests.get("https://www.webscraper.io/test-sites/e-commerce/allinone/computers/tablets")
#Loading the content
content = webpage.content
#Parsing the content
result = BeautifulSoup(content, 'html.parser')
#Identifying the products on the page by div tag and the class name
products = result.find_all("div", {"class" : "col-sm-4 col-lg-4 col-md-4"})
#Creating a list for each of the desired piece of information
names = []
links = []
prices = []

#print(products[0].a.string) #Prints 'Lenovo IdeaTab'
#print(len(products)) #Prints 21 (number of products)


#Iterating over the list of products and extracting the necessary info
for item in products:
    names.append(item.a.string)
    links.append("https://www.websraper.io" + item.a['href'])
    prices.append(item.h4.string)
#Making list of tupples 
data = list(zip(names, prices, links))
#Creating pandas dataframe
df = pd.DataFrame(data, columns = ['Name', 'Price', 'Link'])
#Writing the dataframe in excel file
try:
    df.to_excel("C:\\Users\\David\\Desktop\\Python_WebScraping\\Course\\Products.xlsx")
except:
    print("\nSomething went wrong, check the code")

else:
    print("\nWeb data successfulyy written to excel")

finally:
    print("\nQuitting the program.")
#END 




