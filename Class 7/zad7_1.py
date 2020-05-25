def summary(number):
    score = 0
    if number < 0:
        number *= -1
    for i in str(number):
        score += int(i)
    return score
try:
    x = int(input("Podaj liczbę: "))
    print(summary(x))
except:
    print("Podano nieprawidłowe dane.")