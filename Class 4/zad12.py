lista = []
parzyste = []
for i in range(5):
    number = int(input("Podaj liczbę: "))
    lista.append(number)
for i in range(len(lista)):
    if lista[i]%2==0:
        parzyste.append(lista[i])
print(lista)
print(parzyste)