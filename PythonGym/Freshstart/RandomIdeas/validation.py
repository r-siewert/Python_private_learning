letterList = ["A", "B", "C", "D"]

eingabe = input("Bitte geben Sie einen Buchstaben ein: \n").upper()
gefunden = False

for x in letterList:
    if x in letterList:
        if x == eingabe:
            gefunden = True
            break



if gefunden:
    print("this letter is valid!")
else:
    print("*Warning!* this letter is invalid")

