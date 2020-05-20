code = input("Podaj kod pocztowy: ")
is_code = True
if code[2] == "-" and len(code)==6:
    for i in range(len(code)):
        if i==2:
            continue
        if code[i].isdigit() == False:
            is_code = False
else:
    is_code = False
if is_code == True:
    print(f"Podany kod to {code}")
else:
    print("Podano niepoprawny kod.")
