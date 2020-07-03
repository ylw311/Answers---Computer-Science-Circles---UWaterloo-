def getBASIC():
   list = []
   e = 'END'
   while True:
      i = input()
      if i.endswith(e):
         list.append(i)
         return list
      else:
         list.append(i)
