text = "Python macht heute wieder Spaß"


def analyze_text(text):

    newlist = text.split(" ")
    return len(newlist)



result = analyze_text(text)


print(result)





text = "Python macht heute wirklich sehr viel Spaß"

def analyze_text(text):

    newlist = []

    list = text.split()

    for word in list:
        if len(word) >= 5:
            newlist.append(word)

    return newlist






result = analyze_text(text)    

print(result)



"""
Kurzform für die schleife: newlist = [word for word in words if len(word) >= 5]

!!!!!!!!!!!!!!!!!! WICHTIG FÜR PCAP !!!!!!!!!!!!!!!!!!!

[x for x in numbers if x > 10]

"""

numbers = [3, 8, 12, 5, 21, 7, 14]

def get_even_numbers(numb):

    # evenNumbers = []

    # for numbers in numb:
    #     if numbers % 2 == 0:
    #evenNumbers.append(numbers)
    evenNumbers = [numbers for numbers in numb if numbers % 2 == 0]
    

    return evenNumbers




evenSteven = get_even_numbers(numbers)

print(evenSteven)


