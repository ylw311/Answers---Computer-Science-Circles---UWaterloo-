def findLine(prog, target):
   for i in range(len(prog)):
      spiWords = prog[i].split()
      for l in range(len(spiWords)):
         if target != spiWords[l]:
            continue
         if target == spiWords[l]:
            r = i
   return r
