
def is_cube_root(number):
    if number == 0:
        return "Podana liczba to zero."
    else:
        is_true = False
        if number > 0:
            for i in range(number+1):
                if i*i*i == number:
                    is_true = True
        else:  
            for i in range(number,0,1):
                if i*i*i == number:
                    is_true = True
        if is_true:
            return "Prawda"
        else:
            return "Fałsz"    
                
try:
    x = int(input("Podaj liczbę: "))
    print(is_cube_root(x))
    #test = []
    #for x in range (100000):
    #    if is_square(x) == "Prawda":
    #        test.append(x)
    #print(test)
except:
    print("Podano niepoprawne dane.")