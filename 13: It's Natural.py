def naturalNumbers(n):
   mlist=[]
   for i in range(1, n+1):
      mylist = mlist+[i]
   return mylist
  
#-----or
   
def naturalNumbers(n):
   list = []
   for i in range(n):
      list = list + [i+1]
   return list
