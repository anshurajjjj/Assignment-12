#Write a python script to print first N prime numbers.
n = int(input( "Enter a number: "))
for number in range(1,2*n+n):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
        else:
            print(number)
