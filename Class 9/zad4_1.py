class Mem:
    def __init__(self,name,url,is_favourite=False):
        self.name = name
        self.url = url
        self.is_favourite = is_favourite
answer = "yes"
mems = []
try:
    while answer == "yes":
        mems.append({"name":input("Input name of mem: "),"url":input("Input url adress: "), "is_favourite":input("Is it one of your favourites?\n(True/False)>> ").capitalize()})
        answer = input("Do you want to add another mem?\n>> ").lower()
    print(mems)

    favourites = []
    for mem in mems:
        if mem['is_favourite']== "True" :
            favourites.append(mem)
    print(favourites)

except:
    print("Wrong data added.")