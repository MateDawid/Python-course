import random
wylosowane = []
while len(wylosowane)!=6:
    liczba = random.randrange(1,50)
    if liczba in wylosowane:
        continue
    wylosowane.append(liczba)
print(wylosowane)

