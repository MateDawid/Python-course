name = input("Podaj imię: ")
#for i in range(1,len(name)+1,2):
#    print(name[i])
for i,value in enumerate(name):
    if i%2 == 1:
        print(value)