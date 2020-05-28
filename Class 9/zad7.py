class HighSchool:
    def __init__(self,name,points,distance):
        self.name = name
        self.points = points
        self.distance = distance
schools = []
s1 = HighSchool("LO im. Jana Zamoyskiego",173,15)
schools.append(s1)
s2 = HighSchool("LO im. Mikołaja Kopernika",193,7)
schools.append(s2)
s3 = HighSchool("LO im. Batalionu 'Zoska'",122,6)
schools.append(s3)

max_points = 180
max_distance = 10
max_school = None

for i in schools:
    print(i.name,"needs",i.points,"and is",i.distance,"km away.")
    if i.points <= max_points and i.distance <= max_distance:
        if max_school:
            if i.points > max_school.points:
                max_school = i
        else:
            max_school = i
if max_school:
    print ("Apply for",max_school.name,".")
else:
    print("No appropriate school found.")