import datetime
from dateutil.relativedelta import relativedelta
class Inquiry:
    def __init__(self,name,date):
        self.name = name
        self.date = date
    def __repr__(self):
        return self.name+' '+self.date
    def is_old(self):
        result = self.date+relativedelta(days=14)
        return (result < datetime.date.today())
    
dt = datetime.date(2020,2,14)
dt2 = datetime.date(2020,5,20)
i = Inquiry("Dawid",dt)
i2 = Inquiry("Kuba",dt2)
print(i.is_old())
print(i2.is_old())
print(datetime.date(2020,5,25)+relativedelta(days=2))  #relative delta pozwala na działania na datach 