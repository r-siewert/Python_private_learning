text = "   Python macht heute richtig Spaß   "

def textcleaner(text):
    newlist = text.strip().split()

    return newlist


result = textcleaner(text)

print(result)


text = "   Python macht heute richtig Spaß   "

def textcleaner(text):
    newlist = text.strip().split()
    pwordlist = []
    for pwords in newlist:
        if pwords.startswith("P"):
            pwordlist.append(pwords)

    return pwordlist


result = textcleaner(text)

print(result)





text = "   Python macht heute richtig Spaß und Python macht Spaß   "

def textcleaner(text):
    newlist = text.strip().split()
    fivelenlist = []
    for words in newlist:
        if len(words) >= 5:
            fivelenlist.append(words)

    return fivelenlist


result = textcleaner(text)

print(result)


# fivelenlist = [words for words in newlist if len(words) >= 5]




text = "Python Java C++ Python Ruby Java Python"

def filter_python(text):
    cleaned = text.strip().split()
    pylist = []

    for words in cleaned:
        if words == "Python":
            pylist.append(words)

    return pylist

result = filter_python(text)

print(result)

#[words for words in cleaned if words == "Python"]



text = "Python Java C++ Python Ruby Java Python"

def filter_python(text):
    cleaned = text.strip().split()
    pylist = [words for words in cleaned if words == "Python"] 

    return pylist

result = filter_python(text)

print(result)