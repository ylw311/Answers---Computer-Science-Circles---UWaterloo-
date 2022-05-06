chin = input()
num = ord(chin)

aNum = num + 1

if num == 90:
   aNum = 65

print(chr(aNum))

#----------or

character = input()

if ord(character) == 90:
   print(chr(65))
else:
   print(chr(ord(character)+1))
