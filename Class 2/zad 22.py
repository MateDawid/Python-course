a = int(input("Podaj liczbę 'a': "))
b = int(input("Podaj liczbę 'b': "))
dividers = []
for i in range(1,max(a,b)):
    if a%i == 0 and b%i == 0:
        dividers.append(i)
print(max(dividers))