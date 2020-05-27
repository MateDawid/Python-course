def is_pesel(pesel):
    if len(pesel) == 11:
        for i in pesel:
            if not i.isdigit():
                return False
        return True
    else:
        return False

pesel = input("Podaj pesel: ")
print(is_pesel(pesel))