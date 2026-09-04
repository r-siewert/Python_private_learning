words = ["Python", "Java", "Python"]



def dicCount(words):

    newdic = {}

    for word in words:
        if word in newdic:
            newdic[word] += 1
        else:
            newdic[word] = 1

    return newdic


result = dicCount(words)

print(result)

########################################################################################

words = ["Python", "Java", "Python", "C++", "Java", "Python"]


def dicCount(words):
    newdic = {}

    for word in words:
        if word in newdic:
            newdic[word] += 1
        else:
            newdic[word] = 1

    return newdic        



result = dicCount(words)

############### WICHTIG #####################
maxresult =  max(result, key=result.get)
############### WICHTIG #####################


print(result)

print("Most common: " + maxresult)




