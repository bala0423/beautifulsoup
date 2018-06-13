import requests
from bs4 import BeautifulSoup
import csv

csv_file = csv.writer(open('chennai-market-13-06-2018.csv','w'))

url = 'https://www.livechennai.com/Vegetable_price_chennai.asp'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')

table = soup.find('table', attrs={'class':'table-price1'})

table_row = table.find_all('tr')

for row in table_row:
	name_veg = row.find_all('td')[1].contents[0]
	price_veg = row.find_all('td')[2].contents[0]
	csv_file.writerow([name_veg,price_veg])
	
