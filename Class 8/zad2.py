def is_square(number):
    is_true = False
    for i in range(1,number+1):
        if i*i == number:
            is_true = True
    return is_true

x = int(input("Podaj liczbę: "))
print(is_square(x))