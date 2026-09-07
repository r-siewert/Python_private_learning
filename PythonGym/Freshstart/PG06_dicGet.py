scores = {
    "Anna": 87,
    "Ben": 94,
    "Clara": 91
}

name = "David"

score = scores.get(name)

if score is None:
    print("No score found")
else:
    print(name, score)

    #get() findet den Key nicht → standardmäßig None.


    scores = {
    "Anna": 87,
    "Ben": 94,
    "Clara": 91
}

name = "David"

score = scores.get(name, 0)

if score == 0:
    print("No score found")
else:
    print(name, score)

    #No score found




    inventory = {
    "sword": 3,
    "shield": 1,
    "potion": 5
}

item = "bow"

amount = inventory.get(item, 0)

if amount > 0:
    print(item, amount)
else:
    print(item, "not available")

    #bow not available