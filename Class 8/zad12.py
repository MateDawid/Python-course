import requests
from bs4 import BeautifulSoup
#https://www.otomoto.pl/osobowe/nissan/qashqai/?page=2
def offer (address):
    page = requests.get(address)
    print(page) #sprawdzenie połączenia ze stroną -> 200 oznacza połączenie)
    soup = BeautifulSoup(page.content,"html.parser")
    print(soup.title.text)
    counter = soup.find('span',class_="counter")
    print("="*40)
    print("Wszystkich ofert:", counter.text)
    print("="*40)
    elements = soup.findAll('article',attrs={"class":"adListingItem"})
    print("Ofert na stronie:",len(elements))
    print("="*40)
    for element in elements:
        offerTitle = element.find('h2',class_="offer-title")
        year = element.find('li',attrs = {"data-code":"year"})
        mileage = element.find('li',attrs = {"data-code":'mileage'})
        print("Pojazd:",offerTitle.text.strip())
        print("Rok produkcji:",year.text.strip())
        print("Przebieg:",mileage.text.strip())
        print("="*40) 

url = "https://www.otomoto.pl/osobowe/nissan/qashqai/?page=2"
offer(url)
