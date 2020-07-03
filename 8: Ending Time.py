currentTime = input()
D = int(input())

for p in range(0,len(currentTime)):
    if currentTime[p] == ":":
       colon = currentTime[p]
       hour = int(currentTime[0: p])
       minute = int(currentTime[p+1: len(currentTime)-0])

minutesLeft = minute + D
   
if hour >= 23:
    hour = 0   
    minutesLeft = minutesLeft - 60 

while minutesLeft >= 60:
    minutesLeft = minutesLeft - 60
    hour = hour+1
   
   
hour = int(hour) % 24

for i in range(0,9):
    if i == minutesLeft:
       minutesLeft = "0"+str(minutesLeft)
    if i == hour:
       hour = "0"+str(hour)

if minutesLeft == 9:
   minutesLeft = "0"+str(minutesLeft)
            
print(str(hour)+":"+str(minutesLeft))
