h = int(input("Podaj wysokość: "))
print("Wieża")
for i in range(1,h+1):
    print(i*"*")
print("Choinka")
p = (h-1)
for i in range(1,h+1):
    stars =(2*i-1)*"*"
    przerwa = p*" "
    print(przerwa+stars)
    p -= 1