import random
wylosowane = set()
while len(wylosowane)!=6:
    liczba = random.randrange(1,50)
    wylosowane.add(liczba)
print(wylosowane)