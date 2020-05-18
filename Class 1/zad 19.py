name = input("Podaj imię: ")
if name[-1] != "a" or name == "Barnaba":
    print("Mężczyzna")
elif name[-1] == "a" and name != "Barnaba":
    print("Kobieta")