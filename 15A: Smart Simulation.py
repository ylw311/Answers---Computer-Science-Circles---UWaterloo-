def execute(prog):
  location = 0
  Visited = [False] * len(prog)
  while True:
    if location==len(prog)-1: return "success"
    elif Visited[location] == True: return "infinite loop"  
    Visited[location] = True
    T = prog[location].split()
    
    location = findLine(prog, T[len(T)-1])
