def isPesel(x):
    if len(x)==11 and x.isnumeric():
        return True
    else:
        return False
pesel = input('Podaj PESEL:\n')
print(isPesel(pesel))