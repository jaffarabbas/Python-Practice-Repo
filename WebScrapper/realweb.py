from bs4 import BeautifulSoup
import requests

html_scrapper = requests.get('http://kwsb.gos.pk/Default.aspx').text
print(html_scrapper)
soup = BeautifulSoup(html_scrapper,'lxml')

