decision = "Tak"
lista = []
lista2 = []
while decision == "Tak" or decision == "tak":
    number = input("Podaj element listy: ")
    lista.append(number)
    decision = input("Dodać kolejne elementy? ")
for i in range(1,len(lista),2):
    lista2.append(lista[i])
print(lista)
print(lista2)

