scores = {
    "Anna": 87,
    "Ben": 94,
    "Clara": 91
}


for key, value in scores.items():
    print(key, value)






scores = {
    "Anna": 87,
    "Ben": 94,
    "Clara": 91
}

for key, value in scores.items():
    print(key + ":", value)

print("========================================")


scores = {
    "Anna": 87,
    "Ben": 94,
    "Clara": 91,
    "David": 94
}
    
print(max(scores.values())) #gibt den höchsten wert aus dem dic aus

for number in scores.values(): #gibt alle Werte aus dem dic aus.
    print(number)

print("=========================================")

scores = {
    "Anna": 87,
    "Ben": 94,
    "Clara": 91,
    "David": 94
}

highest = max(scores.values())
print("Highest score:", highest)

for key, value in scores.items():
   if value == highest:
       print(key) 


print("=========================================")


products = {
    "Laptop": 899,
    "Mouse": 25,
    "Keyboard": 75,
    "Monitor": 299,
    "Headset": 120,
    "Webcam": 100
}

limit = 100

for name, price in products.items():
    if price < limit:
        print(name, price)


print("=========================================")


products = {
    "Laptop": 899,
    "Mouse": 25,
    "Keyboard": 75,
    "Monitor": 299
}

for name, price in products.items():
    if price < 100:
        products[name] = price + 10

for name, price in products.items():
    print(name, price)

#name ist jeweils der aktuelle Key der Schleife. Dadurch wird genau der Eintrag verändert, den wir gerade betrachten.

"""
Dictionary lesen
keys(), values(), items()
Dictionary-Werte über Keys verändern
for + if mit Dictionarys kombinieren
Werte filtern und gezielt verändern

"""



products = {
    "Laptop": 899,
    "Mouse": 25,
    "Keyboard": 75
}

mouse_price = products.get("Mouse")
monitor_price = products.get("Monitor")

print(mouse_price)
print(monitor_price)





#Der Vorteil von get() kommt ins Spiel, 
# wenn der Key nicht existiert. 
# Dann gibt get() standardmäßig None zurück, 
# statt direkt einen KeyError auszulösen.


"""
Wichtiges PCAP-Merkstück:

dict[key] → Key fehlt → KeyError
dict.get(key) → Key fehlt → None (standardmäßig)


value = data["x"]

vs.

value = data.get("x")

"""


