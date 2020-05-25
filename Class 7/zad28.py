def fiveString(array):
    result = []
    for i in array:
        if len(i) == 5:
            result.append(i)
    return result

#test
try: 
    print(fiveString(["abc","pięć","sześć","Jakub"]))
except:
    print("Podano nieprawidłowe dane.")