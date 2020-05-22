import random
questions = ["Czy Kopernik była kobietą?","Czy ziemia jest kulą?"]
answers = ["Nie","Tak"]
wylosowane = []
score = 0
while len(wylosowane) != len(questions):
    questionNumber = random.randrange(len(questions))
    if questionNumber in wylosowane:
        continue
    print("Pytanie:",questions[questionNumber])
    wylosowane.append(questionNumber)
    answer = input("Podaj odpowiedź tak/nie: ")
    if answer == answers[questionNumber]:
        score += 1
        print("Prawidłowa odpowiedź.")
    else:
        print("Nieprawidłowa odpowiedź.")
print("Odpowiedziano poprawnie na",score,"pytania.")