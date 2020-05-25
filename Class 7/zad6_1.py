def is_even(number):
        if number%2 == 0:
            return "Liczba parzysta"
        else:
            return "Liczba nieparzysta"
try: 
    a = int(input("Podaj liczbę: "))
    print(is_even(a))
except:
    print("Wprowadzono niepoprawne dane")