def digitalRoot(n):
   if n < 10:
      return n
   else:
      i = digitalRoot(digitalSum(n))
      return i
