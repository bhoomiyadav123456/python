# Read input
weight = float(input("Enter weight (in kg): "))
height = float(input("Enter height (in meter): "))

# Calculate BMI
bmi = weight / (height * height)

# Determine BMI category
if bmi < 18.5:
    print("Underweight - bmi_category.py:10")
elif bmi < 25:
    print("Normal weight - bmi_category.py:12")
elif bmi < 30:
    print("Overweight - bmi_category.py:14")
else:
    print("Obese - bmi_category.py:16")


    '''output:'''
    Enter weight (in kg): 45
    Enter height (in meter): 6.2
    Underweight