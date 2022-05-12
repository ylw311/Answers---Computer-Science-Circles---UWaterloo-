def postalValidate(S):
   if any(char.isdigit() for char in S) == True:
      S = S.replace(' ', '')

      if len(S) == 6 and S[1 and 3 and 5].isdigit() == True and S[0 and 2 and 4].isalpha() == True:
         for n in range(len(S)):
            if S[n].isalpha() == True:
               u = S[n].upper()
               S = S.replace(S[n], u)
            if S[n].isdigit() == True:
               n = int(S[n])
         return S
      else:
         return False
   else:
      return False
   

#-----------or
def postalValidate(S):
   S = S.replace(" ","")
   if (len(S) == 6) and (S[0].isalpha() and S[2].isalpha() and S[4].isalpha() == True) and (S[1].isdigit() and S[3].isdigit() and S[5].isdigit() == True):
      S = S.upper()
      return S
   return False
