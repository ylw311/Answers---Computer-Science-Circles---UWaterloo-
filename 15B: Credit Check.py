def check(S):
   for i in range(len(S)):
      if S[i].isalpha() == True:
         return False
   if len(S) != 19 or S[4 and 9 and 14] != ' ':
      return False
   else: 
      nWithSpace = list(S)
      nlist = S.replace(' ', '')
      result = 0
      for n in range(len(nlist)):
         result = result + int(nlist[n])
      divChe = result/10
      if divChe.is_integer() == True:
         return True
      else:
         return False
