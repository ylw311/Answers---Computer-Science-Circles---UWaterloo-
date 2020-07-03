def nestedListContains(NL, target):
   if isinstance(NL, int):
      return NL
   if NL == target:
      return True
   for i in range(0, len(NL)):
      if NL[i] == target:
         return True
   for s in range(0, len(NL)):
       sub = nestedListContains(NL[s], target)
       if sub == True:
            return True
   return False

