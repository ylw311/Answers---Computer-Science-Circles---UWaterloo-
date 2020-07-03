S = input()
for p in range(0,len(S)):
   if S[p] == "+":
      plus = S[p]
      num1 = int(S[0: p])
      num2 = int(S[p+1: len(S)-0])

print(num1 + num2)
