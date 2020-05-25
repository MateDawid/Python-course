def Pitagoras(x,y,z):
    if a<0 or b<0 or c<0:
        return False
    array = [a,b,c]
    array.sort()
    if array[0]*array[0] + array[1]*array[1] == array[2]*array[2]:
        return True
    else:
        return False

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))

if Pitagoras(a,b,c)==True:
    print("Podane liczby są liczbami pitagorejskimi.")
else:
    print("Podane liczby nie są liczbami pitagorejskimi")