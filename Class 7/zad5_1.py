def is_pitagorean(x,y,z):
    if x>0 and y>0 and z>0:
        array = [x,y,z]
        array.sort()
        if array[0]*array[0] + array[1]*array[1] == array[2]*array[2]:
            return "Liczby pitagorejskie"
        else:
            return "To nie są liczby pitagoresjkie."
    else:
        return "Podano niepoprawne dane."

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
c = int(input("Podaj trzecią liczbę: "))
print(is_pitagorean(a,b,c))