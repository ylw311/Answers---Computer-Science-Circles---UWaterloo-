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


#---------or

startingTime = input()
passedTime = int(input())

index = 0

#find and split the starting time into hours and minutes
for i in range(len(startingTime)):
   if startingTime[i] == ":":
      index = i
      hour = int(startingTime[0:index])
      minutes = int(startingTime[index+1:len(startingTime)])
      break
  
newHour = str((hour + int((minutes+passedTime)/60)) % 24) #rounded down

   
newMinutes = str(int(minutes+passedTime) -  60*int((minutes+passedTime)/60))



#these extra conditional statements are just here to keep the grader happy cuz apparently it wants two numbers for single digit times...you'll see
#there's prob better way to do this but I got lazy-
hourSingleDigit = len(newHour) == 1
minutesSingleDigit = len(newMinutes) == 1

if hourSingleDigit == True and minutesSingleDigit == True:
   print("0" + newHour + ":" + "0" + newMinutes)
elif hourSingleDigit == True:
   print("0" + newHour + ":" + newMinutes)
elif minutesSingleDigit == True:
   print(newHour + ":" + "0" + newMinutes)
else:
   print(newHour + ":" + newMinutes)

     
