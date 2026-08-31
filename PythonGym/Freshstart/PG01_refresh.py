




def get_range(numb):


 largest = max(numb)
 smallest = min(numb)

 result = largest - smallest
 return result


numbers = [4, 7, 12, 3, 20]

solution = get_range(numbers)

print(solution)









def get_range(numb):


 largest = max(numb)
 smallest = min(numb)

 result = largest - smallest
 return result


numbers = [4, 7, 12, 3, 20]

solution = get_range(numbers)

print(solution)





def get_range(*numbers):
 return max(numbers) - min(numbers)

result = get_range(4, 7, 12, 3, 20)

print(result)



def get_stats(*numbers):
 largest = max(numbers)
 smallest = min(numbers)
 
 solution = largest - smallest
 return solution, smallest, largest


result = get_stats(4, 7, 12, 3, 20)

Range, Minimum, Maximum = result

print(f"Range = {Range}")
print(f"Minimum = {Minimum}")
print(f"Maximum = {Maximum}")