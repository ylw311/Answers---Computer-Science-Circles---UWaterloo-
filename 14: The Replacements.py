def replace(list, X, Y):
   count = list.count(X)
   for i in range(count):
      index = list.index(X)
      list.pop(index)
      list.insert(index,Y)
               
