def is_even(x):
    if x%2 == 0:
        return True
    else:
        return False
x = int(input("Podaj liczbę: "))
print(is_even(x))