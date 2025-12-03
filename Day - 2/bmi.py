#If the user enters height as 150 instead of 1.50, what will happen to the BMI calculation?

weight = input("Weight: ")
height = input("Height: ")


weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / (height_as_float ** 2)

bmi_as_int = int(bmi)
print(bmi_as_int)
 