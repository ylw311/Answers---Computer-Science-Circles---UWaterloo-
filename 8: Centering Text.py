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
 
#----------or

width = int(input())

text = input()

while text != "END":
   dots = width - len(text)
   if dots % 2 == 0:
      print("." * int(dots/2) + text + "." * int(dots/2))
   else:
      roundeddown = int(dots/2)
      print("." * (dots-roundeddown) + text + "." * roundeddown)
   text = input()
