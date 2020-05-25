def number_of_divisors(n):
    divisors = 0
    for i in range(1,n+1):
        if n%i == 0:
            divisors += 1
    return divisors

def is_prime(n):
    if number_of_divisors(n)==2:
        return "Liczba pierwsza"
    else:
        return "Liczba złożona"
    
x = int(input("Podaj liczbę: "))
print(is_prime(x))

