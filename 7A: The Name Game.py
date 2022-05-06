name = input()
line1 = name + ", " + name + ", " + "bo-b" + name[1:len(name)-0] 
line2 = "banana-fana fo-f" +  name[1:len(name)-0] 
line3 = "fee-fi-mo-m" +  name[1:len(name)-0] 
line4 = name + "!"

print(line1)         
print(line2)  
print(line3)  
print(line4)  


#--------------or

name = input()
print((name + ", ")*2 + "bo-b" + name[1:len(name)])
print("banana-fana " + "fo-f" + name[1:len(name)])
print("fee-fi-mo-m" + name[1:len(name)])
print(name + "!")
