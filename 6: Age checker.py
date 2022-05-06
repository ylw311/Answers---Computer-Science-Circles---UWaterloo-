age = int(input())
if age >= 18:
   print("You can vote")
if age <= 17 and age >= 0:
   print("Too young to vote")
if age < 0:
   print("You are a time traveller")

 #--------------or

age = int(input())
if age >= 18:
 print("You can vote")
elif age < 0:
 print("You are a time traveller")
else:
 print("Too young to vote")
