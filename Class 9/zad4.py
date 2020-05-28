class Mem:
    #jeśli is_favourite nie zostanie podane, ustaw wartość False, typ domyślny 
    #konstruktor
    def __init__(self,name,url,is_favourite=False):
        self.name = name
        self.url = url
        self.is_favourite = is_favourite
#obiektem jest m i m2, np. klasa = budynek, obiekt = mój dom
m = Mem('Programowanie jest super','http://super.jpg')
m2 = Mem('Jestem Bogiem', 'http://aa.jpg',True)
print(m.name,m.is_favourite)
print(m2.name,m2.is_favourite)
mems = [m,m2]
for mem in mems:
    if mem.is_favourite:
        print(mem.name,mem.url)