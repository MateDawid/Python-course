def PESEL(pesel):
    if pesel.isnumeric() and len(pesel) == 11:
        return "To jest numer PESEL"
    else:
        return "To nie jest numer PESEL." 

x = input("Podaj numer PESEL: ")
print (PESEL(x))