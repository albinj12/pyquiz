import csv

print("Welcome to pyquiz")
print("Available streams are maths, science and GK.\nAll streams have 10 questions in total.\nEvery question have one mark each\n")

score = 0

#quizStream = input("Select quiz subject : ")

with open('maths.csv','r') as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        ans = input(row[0]+" : ")
        if ans == row[1]:
            score += 1


print("Total score is " + str(score))

