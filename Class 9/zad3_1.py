class Person:
    def __init__(self,name,surname,pesel):
        self.name = name
        self.surname = surname
        self.pesel = pesel

p = Person("Dawid","Mateusiak","96040312345")
print(p.name,p.surname,p.pesel)
