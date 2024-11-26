# creating the algorithm
w = float(input("Enter your weight(in kg): "))
h = float(input("Enter your height(in metres): "))
bmi = w / (h * h)
print("Your bmi is",bmi)
if (bmi < 18.5):
    print("you are underweight.")
elif (18.5 <= bmi and bmi < 24.5):
    print("you are healthy.")
elif (24.5 <= bmi and bmi <= 30):
    print("you are overweight.")
elif (bmi > 30):
    print("you are obese")
