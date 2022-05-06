n=int(input())
for i in range(0, n):
  X = 0
  for j in range(i,n):
    X = (X*10)+1
  print(X)

  
  #--------or
  
n=int(input())
for i in range(n):
   print("1" * (n-i))
