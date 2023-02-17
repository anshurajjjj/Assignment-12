#Write a python script to calculate HCF of two numbers.
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
for i in range(1, min(x, y)):
    if x % i == 0 and y % i == 0:
        HCF = i
print("HCF of", x, "and", y,  "is", HCF)
