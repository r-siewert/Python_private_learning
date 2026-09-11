x = ord(input("Gib einen Buchstaben ein: "))


#Hier ist x eine Zahl
print(x)

y = x - 5

print(y)

print(chr(y))


"""
Methoden zur ASCII-UmwandlungAls Liste von Zahlen (List Comprehension):
Code: [ord(char) for char in "wort"]Ergebnis: [119, 111, 114, 116]Beschreibung: 
Wandelt jeden Buchstaben einzeln um und speichert die Zahlen in einer Liste.
"""


"""
Als zusammenhängender Text (String):
Code: " ".join(str(ord(char)) for char in "wort")
Ergebnis: "119 111 114 116"Beschreibung: 
Erstellt eine lesbare Textkette, bei der die ASCII-Werte durch Leerzeichen getrennt sind.
Einzelnen Buchstaben umwandeln:Code: ord('w')Ergebnis: 
119Beschreibung: Liefert den exakten Zahlenwert für ein einzelnes Zeichen.
"""


"""
Der umgekehrte Weg (ASCII zurück in Text)
Falls Sie die Zahlen wieder in ein Wort verwandeln möchten, 
nutzen Sie die Funktion chr() laut der offiziellen Python-Dokumentation:
Code: "".join(chr(zahl) for zahl in [119, 111, 114, 116])
Ergebnis: "wort"Lassen Sie mich wissen, falls Sie:
Die Werte lieber im Hexadezimal- oder Binärformat benötigen.
Die Zahlenwerte direkt in Byte-Objekte (bytes) konvertieren möchten.
"""


uWort = input("Gib ein, was verschlüsselt werden soll: ")

for buchstabe in uWort:
    verBuchstabe = (ord(buchstabe)) + 3
    print(chr(verBuchstabe),end="")


print()
print()


# Entschlüsserlung
vWort = input("Gib ein, was entschlüsselt werden soll: ")

for buchstabe in vWort:
    norBuchstabe = (ord(buchstabe)) - 3
    print(chr(norBuchstabe),end="")