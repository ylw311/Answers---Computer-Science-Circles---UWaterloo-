def calculateCelsius(degreeC):
   num = inp[:-1]
   c = float(num)
   f = c * (9/5) + 32
   result = str(f)+'F'
   return result

def calculateFahrenheit(degreeF):
   num = inp[:-1]
   f = float(num)
   c = (f-32) * (5/9)
   result = str(c)+'C'
   return result

inp = str(input())
loca = len(inp)-1

if inp[loca] == 'C':
   print(calculateCelsius(inp))
elif inp[loca] == 'F':
   print(calculateFahrenheit(inp))
