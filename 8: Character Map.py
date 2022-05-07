index = 32
#there are 12 rows, 6 sets of rows
for i in range(6):
   print("chr:  ", end='')
   #there are 16 characters per row
   for a in range(16):
      print(chr(a+index) + "   ", end='')
      
   
   #add space
   print("")
   
   print("asc: ", end='')
   for b in range(16):
      print(str(b+index), end='')
      if len(str(b+index)) == 2:
        print("  ", end='')
      elif len(str(b+index)) == 3:
        print(" ", end='')
   index += 16
   #add space
   print("")
                                                                                          
