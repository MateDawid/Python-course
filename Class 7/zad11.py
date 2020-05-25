def number_of_divisors(n):
    divisors = 0
    for i in range(1,n+1):
        if n%i == 0:
            divisors += 1
    return divisors

n = int(input("Podaj liczbę: "))
print("Liczba",n,"posiada",number_of_divisors(n),"dzielników.")