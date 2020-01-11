import csv

studName = input("Please enter your name : ")
print("\nHey "+studName+", Welcome to pyquiz")
print("\nAvailable streams are maths, science and GK.\nAll streams have 10 questions in total.\nEvery question have one mark each\n")

stream = ["maths","science","gk"]
score = 0



while True :
    quizStream = input("Select quiz subject : ")
    if quizStream.lower() not in stream:
        print("\nYou had entered a wrong choice.Please choose Maths, Science or GK")
        continue
    else:
        break
    
filename = quizStream.lower()+".csv"

with open(filename,'r') as csvFile:
    csvReader = csv.reader(csvFile)
    for row in csvReader:
        ans = input(row[0]+" : ")
        if ans == row[1]:
            score += 1


print("Total score is " + str(score))

