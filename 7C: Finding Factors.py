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
