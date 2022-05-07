S = input()
for p in range(0,len(S)):
   if S[p] == "+":
      plus = S[p]
      num1 = int(S[0: p])
      num2 = int(S[p+1: len(S)-0])

print(num1 + num2)

#-----or

S = input()
index = 0
for i in range(len(S)):
   if S[i] == "+":
      index = i
      break
      
print(int(S[0:index]) + int(S[index:len(S)]) )
