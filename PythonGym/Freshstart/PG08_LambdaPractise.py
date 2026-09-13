numbers = [4, 7, 2, 9, 5, 8]

for number in numbers:
    if number > 5:

        print(number)


print("===========================================")


numbers = [4, 7, 2, 9, 5, 8]
number = list(filter(lambda x: x > 5, numbers))
print(number)



""""
lambda entscheidet was geprüft wird.
filter() entscheidet welche Elemente durchgelassen werden.
list() macht aus dem Ergebnis wieder eine Liste.
"""
print("===========================================")

numbers = [3, 8, 11, 4, 15, 6, 10]

number = list(filter(lambda x: x % 2 == 0, numbers))
print(number)

print("===========================================")

words = ["Python", "Java", "C++", "Ruby", "JavaScript", "Go"]

word = list(filter(lambda x: len(x) > 3, words))
print(word)

print("===========================================")


numbers = [4, 7, 2, 9, 5, 8]

for number in numbers:
    if number > 5:
        print(number)

print("===========================================")

number = list(filter(lambda x: x > 5, numbers))
print(number)

