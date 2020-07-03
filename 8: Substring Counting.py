needle = input()
haystack = input()
count = 0

for i in range(0,len(haystack)):
   if haystack[i:len(needle)+i] == needle:
      count = count+1
      
print(count)
