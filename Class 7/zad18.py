def last_element(x):
    return x[len(x)-1]

elements = []
num = int(input("Podaj liczbę elementów: "))
for i in range(num):
    element = input("Podaj element tablicy: ")
    elements.append(element)
print(elements)
print(last_element(elements))