import math
   
n=int(input())
   
checkN = 0

while checkN < n-1:
   checkN = checkN + 1
   checkNI = int(math.sqrt(checkN))
   if math.sqrt(checkN) == checkNI:
      print(checkN)
   if math.sqrt(checkN) != checkNI:
      continue

#----------or
n=int(input())
count = 1
while count*count <n:
   print(count*count)
   count+=1  
