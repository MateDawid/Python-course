import requests as r
from bs4 import BeautifulSoup

url = 'https://pogoda.onet.pl/prognoza-pogody/jaworzno-296548'
response = r.get(url)
print(response.text)
#soup = BeautifulSoup(response.text,'html.parser')

#temp = soup.select('.temp') #"." żeby znaleźć po klasie
#print(temp[0].text)