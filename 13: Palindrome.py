def isPalindrome(S): 
   for i in range(len(S)):
      if S[i] == S[-(i+1)]:
         continue
      else: return False 
   return True
