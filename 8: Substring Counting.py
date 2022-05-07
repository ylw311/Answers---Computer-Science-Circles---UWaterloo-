needle = input()
haystack = input()
count = 0

for i in range(len(haystack)):
   if haystack[i:i+len(needle)] == needle:
      count+=1
   
print(count)
