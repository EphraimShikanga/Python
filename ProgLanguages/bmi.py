from math import pow

def calculate_bmi(weight, height):
    bmi = weight / (pow(height, 2))
    if bmi < 18.5:
        return bmi, "Underweight"
    elif bmi < 25:
        return bmi, "Normal weight"
    else:
        return bmi, "Overweight"

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi, interpretation = calculate_bmi(weight, height)

print(f"From Your BMI of {bmi:.2f} you are {interpretation}")