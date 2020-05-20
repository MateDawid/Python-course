number = int(input("Podaj liczbę: "))
dividers = []
for i in range(1,number+1):
    if number%i == 0:
        dividers.append(i)
print(len(dividers))