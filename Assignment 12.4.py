u = int( input( "Enter a upper limit: "))
l = int( input( "Enter a lower limit: "))

for num in range(u, l):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
