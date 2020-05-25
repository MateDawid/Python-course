def first_element(x):
    return x[0]

elements = []
num = int(input("Podaj liczbę elementów: "))
for i in range(num):
    element = input("Podaj element tablicy: ")
    elements.append(element)
print(elements)
print(first_element(elements))