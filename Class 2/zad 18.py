name = input("Podaj imię: ")

#lenght = len(name)
#for i in range(1,len(name),2):
#    print(name[i])

for i,value in enumerate(name):
    if i%2 == 1:
        print(value)