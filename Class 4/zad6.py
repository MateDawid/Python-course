numbers = []
size = int(input("Podaj liczbę elementów: "))
for i in range(1,size+1):
    element = int(input("Podaj liczbę: "))
    numbers.append(element)
summary = 0
for value in numbers:
    summary += value
print(summary)