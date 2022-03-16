import urllib.request
from bs4 import BeautifulSoup
import urllib.error
import time

# Bitcoin price notification every hour

def priceConverter(price):

	'''
	Converts dollar amount to pounds
	'''

	USD = 1 # Flat rate for reference

	GBP = 1.38 # Conversion rate (could scrape this hard coding is not efficient)

	gbpPrice = round((price / GBP)*USD, 2) # Simple convertion

	return gbpPrice

def execute_unix(inputcommand):

   p = subprocess.Popen(inputcommand, stdout=subprocess.PIPE, shell=True)
   (output, err) = p.communicate()

   return output

def scraper():

	'''
	Scrapes current BTC price
	'''

	priceList = []

	# Scraping process: 
	url = 'https://cointelegraph.com/bitcoin-price-index'
	page = urllib.request.urlopen(url)
	pars = BeautifulSoup(page, 'html.parser')
	price = pars.find('span',attrs={'class':'price-value'})
	
	# Extract price from HTML String:
	for chars in price:
		priceList.append(chars)
	
	# Strip all useless characters from string ('$' ',') and convert to int
	strippedPrice = priceList[0][2:-1]
	strippedPrice = strippedPrice.replace(',','')
	strippedPrice = int(strippedPrice)

	# Return val through price converter
	return priceConverter(strippedPrice)

def main():

	# Collect price every hour. Do something based on whether price goes up or down:
	while True:
		currentPrice = scraper()
		print(f"Current Bitcoin Price: £{currentPrice}")
		time.sleep(1) # Updates Every Hour
		newPrice = scraper()
		if newPrice < currentPrice:
			currentPrice = newPrice
			print(f"Bitcoin going down")
		elif newPrice > currentPrice:
			currentPrice = newPrice
			print(f"Bitcoin going up")

main()
