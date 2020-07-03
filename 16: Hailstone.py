def hailstone(n):
   print(n)
   if n == 1:
      return n
   if (n % 2) == 0:
      hailstone(int(n/2))
   else:
      hailstone(int(3*n+1))
      
