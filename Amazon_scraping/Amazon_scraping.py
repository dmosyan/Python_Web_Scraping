import requests
from bs4 import BeautifulSoup
from lxml import html
import smtplib
import time


#example link from amazon. Not every website will accept this kind of traffic
URL = 'https://www.amazon.com/Acer-Predator-Overclockable-Aeroblade-PH315-51-78NP/dp/B07CTHLX8C/'
#for your User-Agent goole in the search bar 'My user-agent'
headers ={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
	page = requests.get(URL, headers=headers)

	soup = BeautifulSoup(page.content, 'lxml')
	title = soup.find(id="productTitle").get_text()

	price = list(soup.find("span", class_="a-price-whole"))
	print(f"The price is: ", "$",price[0])
	print(title.strip())

	if(int(price[0]) < 990):
		send_email()

def send_email():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	password = 'XXX'
	server.login('example@gmail.com', password)

	subject = 'Price fell down'
	body = 'Check the link: https://www.amazon.com/Acer-Predator-Overclockable-Aeroblade-PH315-51-78NP/dp/B07CTHLX8C/'

	msg = f"Subject: {subject}\n\n{body}"

	server.sendmail(
		'example@gmail.com', #sender email
		'example@gmail.com', #reciever email
		msg
		)


	
	server.quite()
	print("Email has beed sent")



#while(True):
check_price()
print("Message sent succesfully")
	#time.sleep(60) #will check every 60 second, increase the time
