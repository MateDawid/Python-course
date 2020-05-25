def number_of_divisors(number):
    score = 0
    for i in range(1,number+1):
        if number%i == 0:
            score += 1
    return score

#try:
#    x = int(input("Podaj liczbę: "))
#    print(f"Liczba {x} posiada {number_of_divisors(x)} dzielników.")
#except:
#    print("Podano niepoprawne dane.")