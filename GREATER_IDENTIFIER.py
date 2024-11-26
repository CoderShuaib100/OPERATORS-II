# creating the algorithm
print("Do not enter decimal values.")
a = int(input("Enter a number1: "))
b = int(input("Enter a number2: "))
c = int(input("Enter a number3: "))

if (a>b and a>c):
    print(a,"is the greatest.")
elif (b>a and b>c):
    print(b,"is the greatest.")
elif (c>a and c>b):
    print(c,"is the greatest.")
elif (a == b and a==c):
    print("All the numbers are equal.")