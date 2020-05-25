def divide(x,y):
    return(x/y) 
a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))
try: 
    print(divide(a,b))
except:
    print("Nie wolno dzielić przez zero!")
