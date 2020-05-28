class Apartment:
    def __init__(self,dict):
        self.city = dict['city']
        self.price_per_meter = dict['price_per_meter']
        self.area = dict['area']
    def full_price(self):
        return round(self.area * self.price_per_meter * 0.95,2)
    def print_description(self):
        print(self.city,self.full_price())
    def __repr__(self): #umożliwia użycie print() na obiekcie
        return self.city+' '+str(self.full_price())
apartament = Apartment({'city':'Warszawa', 'price_per_meter': 10000, 'area': 50.29})
apartament2 = Apartment({'city':'Kraków', 'price_per_meter':8000, 'area': 79})
apartament.print_description()
apartament2.print_description()
print('Repr wywolanie:',apartament )