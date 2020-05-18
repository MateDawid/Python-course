try:
    number = int(input("Podaj liczbę: "))
    if number%2 == 0:
        print("Liczba", number, "jest parzysta")
    elif number%2 == 1:
        print("Liczba", number, "jest nieparzysta")
except:
    print("Wprowadzono niepoprawne dane.")