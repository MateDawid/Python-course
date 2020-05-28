class Apartment:
    def __init__(self,city,area,price_per_meter):
        self.city = city
        self.area = area
        self.price_per_meter = price_per_meter
    def __repr__(self):
        return "Apartment in "+self.city+" costs "+str(round(self.area*+self.price_per_meter,2))+"."
    def get_full_price(self):
        print("Mean price is "+str(round(0.95*self.area*self.price_per_meter,2))+".")

a1 = Apartment("Jaworzno",45,4000)
a2 = Apartment("Chrzanów",42,3800)
print(a1)
a1.get_full_price()
print(a2)
a2.get_full_price()
