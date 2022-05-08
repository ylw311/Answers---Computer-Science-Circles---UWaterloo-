def lowerChar(char):
   if char >= "A" and char <= "Z":
      return chr(ord(char) + 32)
   return char

def lowerString(string):
   result = ""
   for i in range(len(string)):
      result = result + lowerChar(string[i])
   return result
