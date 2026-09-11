print("Welcome to the split your bill calculator!")


#Variables for the App: billTotal, tip, persons, billPer
billTotal = float(input("What was the total bill? "))
tipChoice = int(input("How much % tip would you like to give? 10, 12 or 15? "))
persons = int(input("How many people to split the bill? "))


#Calc for the %
tip = billTotal * (tipChoice / 100)


#Output with Cćalc and round method
print("Each person should pay:",round(((billTotal + tip) / persons), 2),"$")