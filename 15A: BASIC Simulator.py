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

def findLine(prog, target):
   for i in range(len(prog)):
      spiWords = prog[i].split()
      for l in range(len(spiWords)):
         if target != spiWords[l]:
            continue
         if target == spiWords[l]:
            r = i
   return r


def execute(prog):
  location = 0
  Visited = [False] * len(prog)
  while True:
    if location==len(prog)-1: return "success"
    elif Visited[location] == True: return "infinite loop"  
    Visited[location] = True
    T = prog[location].split()
    
    location = findLine(prog, T[len(T)-1])

print(execute(getBASIC()))
