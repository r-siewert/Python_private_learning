scores = {
    "Anna": 72,
    "Ben": 88,
    "Clara": 95,
    "David": 81
}

for name, score in scores.items():
    if score >= 80:
        scores[name] = score + 5

print(scores)


#alle bis auf anna erhalten einen erhöhten wert um +5


scores = {
    "Anna": 72,
    "Ben": 88,
    "Clara": 95,
    "David": 81
}

for name, score in scores.items():
    if score >= 80:
        scores[name] = score + 5
    else:
        scores[name] = 0

print(scores)

#alle bis auf clara erhalten einen erhöhten wert um +10

scores = {
    "Anna": 72,
    "Ben": 88,
    "Clara": 95,
    "David": 81
}

for name, score in scores.items():
    if score >= 80:
        scores[name] = score + 5
    else:
        scores[name] = 0

print(scores)

"""

get(key, default) → „Wenn nicht vorhanden, nimm default.“
dict[key] = value → „Setze diesen Wert tatsächlich.“

"""


inventory = {
    "sword": 3,
    "shield": 0,
    "potion": 5,
    "bow": 1
}

for item, amount in inventory.items():
    if amount == 0:
        inventory[item] = 2
    else:
        inventory[item] = amount + 1

print(inventory)

#amount == 0 → Wert wird auf 2 gesetzt
#sonst → aktuellen Wert nehmen und +1

scores = {
    "Anna": 70,
    "Ben": 85,
    "Clara": 90
}

for name, score in scores.items():
    if score < 80:
        scores[name] = 80

print(scores)

#===========================================

scores = {
    "Anna": 70,
    "Ben": 85,
    "Clara": 90
}

for name, score in scores.items():
    if score < 90:
        scores[name] = score + 10

print(scores)


#=============================================

double = lambda x: x * 2

result = double(7)

print(result)

"""
def double(x):
    return x * 2
"""

#============================================

triple = lambda x: x * 3

result = triple(4)

print(result)

#Parameter x → Ausdruck x * 2 → Ergebnis wird zurückgegeben.

numbers = [2, 7, 4, 9, 1, 6]

result = list(filter(lambda x: x > 5, numbers))

print(result)

#[7, 9, 6]


numbers = [3, 8, 11, 4, 15, 6]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

#[8, 4, 6]