quiz = {"Czy Polska leży w Europie?":"tak","Czy 2+2=5?":"nie","Czy Python to język programowania?":"tak","Czy Warszawa to stolica Polski?":"tak"}
score = 0
for question in quiz:
    answer = (input(question+" =>>")).lower()
    if answer == quiz[question]:
        score += 1
print("Zdobyłeś",score,"punktów.")