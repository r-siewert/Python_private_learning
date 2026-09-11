
import datetime

auswahl = 0
snitch = []

with open("datei.csv", "r") as file: #muss noch die Zeit mit abrufen, damit sie später auch bei 3. mit angezeigt wird.
    for line in file:
        snitch.append(line.strip())

while True:

    print("Willkommen in der snitch Liste! Was wollen Sie tun?: ")
    print("1. Namen hinzufügen")
    print("2. Namen entfernen")
    print("3. Alle Namen anzeigen")
    print("4. Programm beenden")

    auswahl = input("Bitte wählen Sie aus: ")

    if auswahl == "1":
        name = input("Welchen Namen wollen Sie eintragen?: ")
        jetzt = datetime.datetime.now()

        eintrag = jetzt.strftime("%d.%m.%Y %H:%M") + ";" + name

        snitch.append(eintrag)


        with open("datei.csv", "a") as file:
            file.write(name + "\n")

        print("Der name", snitch[-1], "wurde hinzugefügt")
    elif auswahl == "2":
        name = input("Welcher Name soll entfernt werden? ")
        if name in snitch:
            snitch.remove(name)
            print("Der Name", name, "wurde entfernt!")
        else: print("Der Name befand sich nicht in der Liste!")
    elif auswahl == "3":
        print(snitch)
    elif auswahl == "4":
        print("Das Programm beendet sich nun! Auf Wiedersehen!")
        break    
print("Programm beendet!")

