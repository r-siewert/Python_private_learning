#Hier entsteht nur ein kleines Projekt in Form einer "snitch - Liste" in der Schüler der CBW eingetragen werden, die vor 16 Uhr den Teams Call verlassen!!!
#Diese Liste wird jeden tag über eine Input Funktion erweitert ( ich vermute hier eine append funktion für entweder eine normale liste, oder einer externen Datei in der die Liste angefertigt wird.)
#Desweiteren wird ein Frontend benötigt, wie schon beim Einkaufsmenü, welches mehrere abfragen macht und tasten mit dem Menü interagieren lässt.
#Es ist wünschenswert, dass pro eingabe auch eine Art Eingabebestätigung erfolgt. 
#Jeweils Freitags kann man sich die Daten ausgeben lassen und zeigen lassen, wer prozentual am häufigsten vor 16 Uhr fehlt.
#Man kann sogar darüber diskutieren, ob man nicht noch eine Reverseliste anfertigt, die zeigt, wer immer zu spät kommt.. und somit kann man mehrere Ergebisse in unterschiedlichen Verhältnissen ausgeben.
#geheim top kandidat DaniSahne, Janina Riley, Maik Kasperle, Joachim Haacke, JHONNY "NOT THE KID" RAULEDER
#perfekte addition: Uhrzeit und Datum zum jeweiligen Eintrag des Names machen und darstellen



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

