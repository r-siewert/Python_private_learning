text = "Python Java Python Ruby Java Python C++"


def dicWordCounter(text):
    newlist =  text.split()

    newdic = {}
    

    for words in newlist:
        # newdic[words] = count            
        # if words == words in newdic:
        #     count += 1
        count = 0 
        for word in newlist:
            if word == words:
                count += 1

        newdic[words] = count           
     
    return newdic




result = dicWordCounter(text)    
print(result)





text = "Python Java Python Ruby Java Python C++"


def dicWordCounter(text):
    newlist =  text.split()

    newdic = {}

    for words in newlist:
        if words not in newdic:
            newdic[words] = 1
        else: 
            newdic[words] += 1


    return newdic

result = dicWordCounter(text)

print(result)
    