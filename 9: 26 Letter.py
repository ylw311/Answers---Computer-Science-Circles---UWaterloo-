letter = input()

if letter>=chr(65) and letter<=chr(90):
    print((ord(letter)-64))
else:
    print('invalid')
    
#----or
#note: python does string comparisons: https://cscircles.cemc.uwaterloo.ca/console/?consolecode=%23%20if%20first%20letter%20is%20different%2C%20string%20starting%20closer%20to%20A%20is%20smaller%0Aprint%28%27apple%27%20%3C%20%27banana%27%29%20%23%23%20gives%20True%0A%23%20but%20capital%20letters%20are%20smaller%20than%20non-capital%20ones.%20%28because%20of%20ord%28%29%29%0Aprint%28%27Zebra%27%20%3C%20%27abacus%27%29%20%23%23%20gives%20True%0A%23%20if%20first%20letters%20are%20identical%2C%20we%20compare%20the%20second%20letters%2C%20etc%0Aprint%28%27apple%27%20%3C%20%27aquarium%27%29%20%23%23%20gives%20True%0Aprint%28%27aquarium%27%20%3C%20%27aquarius%27%29%20%23%23%20gives%20True%0A%23%20if%20all%20letters%20are%20the%20same%20but%20one%20string%20is%20shorter%2C%20shorter%20is%20smaller%0Aprint%28%27aqua%27%20%3C%20%27aquarium%27%29%20%23%23%20gives%20True%0A

letter = input()

if letter>='A' and letter<='Z':
    print(ord(letter)-64)
else:
    print('invalid')
    
