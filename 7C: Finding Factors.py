import math

n = int(input())

count = 0

while count < n:
   count = count + 1
   counti = int(n/count)
   if n/count == counti:
      print(count , "times" , int(n/count) , "equals" , n)
   if n/count != count:
      continue

      
#--------------or

n = int(input())
for i in range(n):
   if n % (i+1) ==0:
      print(str(int(i)+1) + " times " + str(int(n/(i+1))) + " equals " + str(n))
