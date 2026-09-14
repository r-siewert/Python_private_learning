numbers = [4, 7, 2, 9, 5, 8]
result = [number for number in numbers if number > 5]
print(result)

print("=============================")

numbers = [3, 8, 11, 4, 15, 6, 10]
result = [ number for number in numbers if number % 2 == 0]
print(result)

print("==============================")

numbers = [3, 8, 11, 4, 15, 6, 10]
result = [ number * 2 for number in numbers if number % 2==0]
print(result)


"""
[number * 2 | for number in numbers | if number % 2 == 0]
     ↑                ↑                    ↑
  WAS kommt       WO kommt es her?     WELCHE dürfen rein?
  """

print("====================")

numbers = [2, 5, 8, 11, 14, 17, 20]
result = [number * 3 for number in numbers if number % 2 != 0]
print(result)

print("=====================")

numbers = [2, 5, 8, 11, 14, 17, 20]
result = [number * 5 for number in numbers if number % 2 == 0]
print(result)

print("=======================")

numbers = [2, 5, 8, 11, 14, 17, 20]
result = [number % 2==0 * 5 for number in numbers]

print(result)

print("===============")

numbers = [2, 5, 8, 11, 14, 17]

result = [number * 2 if number %2 == 0 else number for number in numbers]

print(result)