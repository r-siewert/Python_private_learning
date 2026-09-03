text = "   Python macht heute richtig Spaß und Python ist ziemlich cool   "

def cleanLenGiver(lyste):   
    cleanedlist = lyste.strip().split()
    

    newlist = [word for word in cleanedlist if len(word) >= 5 ]

    return newlist




result = cleanLenGiver(text)    

print(result)