#print(letterGoodness) #testing... it's predefined
code = input()

for S in range(26):
 
   
   list = []
   for i in range(len(code)):
      numO = ord(code[i])
      numC = numO + S #shift value
      if numC > 90:
         numC = numC-90 + 64
      
      if numC < 65:
         numC = numC-65+91
      list.append(chr(numC))
      print(list)
      
      #if S == 1:
      #write about lettergoodness and store it under some variable (S??)
      
#change symbol back to space      
#list
#list.replace('%', ' ')
