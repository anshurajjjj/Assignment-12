#Write a python script to calculate LCM of two numbers.
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
if x > y:
  x, y = y, x
for i in range(1,x+1):
  if x%i == 0 and y%i == 0:
    gcd = i

LCM = (x*y)/gcd

print("LCM is", LCM)
