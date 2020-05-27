import requests as r
response = r.get('https://api.nbp.pl/api/cenyzlota/2020-05-20?format=json') #łączy ze stroną
json = response.json() #type(json) == lista
gold = json[0]         #type(gold) == dict
print("Cena złota to", gold['cena'],"zł.")

# krótsze rozwiązanie - json[0]['cena']