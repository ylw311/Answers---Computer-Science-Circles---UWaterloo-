width = int(input())
while True:
  
   text = input()
   
   if text == 'END':
      break
   
   else:
      T = len(text)
      RS = ((width-T)//2)
      LS = (width-RS-T)
   
      LD = LS * "."
      RD = RS * "."
   
      print(LD+text+RD)
 
