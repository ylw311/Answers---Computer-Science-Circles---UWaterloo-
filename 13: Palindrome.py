def isPalindrome(S): 
   for i in range(len(S)):
      if S[i] == S[-(i+1)]:
         continue
      else: return False 
   return True

#or a more unnecessary complicated version lol (which may help understand or be more intuitive to some?)

import math

def isPalindrome(S):
   #if even number
   if len(S)%2==0:
       for i in range(math.ceil(len(S)/2)):
            if S[i] == S[-(i+1)]:
               continue
            else:
               return False
       return True
   #if odd number
   elif len(S)%2!=0:
       for i in range(int(len(S)/2)):
            if S[i] == S[-(i+1)]:
               continue
            else:
               return False
       return True
