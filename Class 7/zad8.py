def is_square(number):
    if number > 0:
        root = number**(0.5)
        if round(root)*round(root) == number:
            return "Prawda"
        else:
            return "Fałsz"
    elif number == 0:
        return "Podana liczba to zero."
    else:
        return"Nie można uzyskać pierwiastka liczby ujemnej"
try:
    x = int(input("Podaj liczbę: "))
    print(x**(0.5))
    print(is_square(x))
    #test = []
    #for x in range (100000):
    #    if is_square(x) == "Prawda":
    #        test.append(x)
    #print(test)
except:
    print("Podano nieprawidłowe dane.")
