def lowerChar(char):
   if char >= "A" and char <= "Z":
      return chr(ord(char) + 32)
   return char
