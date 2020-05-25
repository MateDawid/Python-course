def sum(x):
    score = 0
    for i in range (len(x)):
        score += int(x[i])
    return score
x = input("Podaj liczbę: ")
print(sum(x))