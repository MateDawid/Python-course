#Klasa = definicja dla obiektu
# Klasa to nowy typ!!!

class Person: 
    #funkcje, ktore sa w programowaniu obiektowym wewnatrz klasy, nazywamy metodami
    #__init__ = konstruktor, specjalna metoda, która tworzy obiekt
    def __init__(self,name,surname,pesel):
        #moje imie = imie, ktore pochodzi z argumentu funkcji
        self.name = name
        self.surname = surname
        self.pesel = pesel
#konkretny element klasy = obiekt
p = Person('Adam','Kowalski','12121232123')
print(p.name,p.surname)