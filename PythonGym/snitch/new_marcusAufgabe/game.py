inventory = {
    "waffe": "Keule",
    "ruestung": "Lederharnisch",
    "leben": 100
}
x = inventory["waffe"]
print(x)

inventory["waffe"] = "Schwert"
x = inventory["waffe"]

print("Du hast ein " + x + " gefunden!")

inventory.update({"schild": "Holzschild"})
x = inventory["schild"]

print("Du hast ein " + x + " gefunden!")

dmg = 20
inventory["leben"] = 100 - dmg
print("Du erhälst " + str(dmg) + " Schaden, da du hingefallen bist!")


print(inventory)

def heiltrank(inventory, betrag):
    inventory["leben"] = min(inventory["leben"] + betrag, 100)
    print("Du heilst dich um " + str(betrag) + " Lebenspunkte!")

heiltrank(inventory, 35)

print(inventory)