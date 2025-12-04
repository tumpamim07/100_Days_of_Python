weight = int(input("Enter your weight "))
height = float(input("Enter your height "))

bmi = weight / (height ** 2)

if bmi >= 18.5:
    print("normal weight")
elif bmi >= 25:
    print("overweight")
else: 
    print("underweight")