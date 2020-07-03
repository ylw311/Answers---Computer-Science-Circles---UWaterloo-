def digitalSum(n):
  if n < 10:
      return n
  else: 
      s = digitalSum(n//10)
      s = s + n%10
      return s
