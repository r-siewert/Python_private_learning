weight = 185
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇


#<18,5 = underweight, 18,5 - 24,9 = normal, 25-29,9 = overweight


if bmi >= 25:
    print("You are an overweight fat fuck")
elif bmi >= 18.5 and bmi <= 24.9:
    print("You have normal weight")
else:
    print("You need to eat more, you little sceleton")