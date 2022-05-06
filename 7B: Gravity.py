import math
sV = input()
v = float(sV)
t = v**2 - 4*-4.9*11000
sq = math.sqrt(t)   
t = (v - sq) / (2*-4.9)
print(t)

#----or

import math
v = float(input())
print((v-math.sqrt(v**2-4*(-4.9)*(11000)))/(2*(-4.9)))
