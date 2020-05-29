class HighSchool:
    def __init__(self,name,distance,points):
        self.name = name
        self.distance = distance
        self.points = points
    def __repr__(self):
        return self.name+" is "+str(self.distance)+"km away and needs "+str(self.points)+"points"

schools = []
s1 = HighSchool("LO im. Jana Zamoyskiego",15,173)
s2 = HighSchool("LO im. Mikołaja Kopernika", 7,193)
s3 = HighSchool('LO im. Batalionu "Zoska"',6,122)
schools.append(s1)
schools.append(s2)
schools.append(s3)

max_points = 180
max_distance = 10
max_school = None
for school in schools:
    print(school)
    if school.distance <= max_distance and school.points <= max_points:
        if max_school:
            if school.points > max_school.points:
                max_school = school
        else:
            max_school = school
if max_school:
    print("Apply for "+max_school.name)
else:
    print("No school found.")   