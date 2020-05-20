n = int(input("Podaj liczbę: "))
strong1 = 1
strong2 = 1
for i in range(1,n+1):
    strong1 *= i
    if i == n-2:
        strong2=strong1
print(2*(strong1+strong2))
