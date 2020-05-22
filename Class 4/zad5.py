number = []
size = int(input("Podaj liczbę elementów: "))
for i in range(1,size+1):
    element = int(input("Podaj liczbę: "))
    number.append(element)
print(number)
print(number[::-1])