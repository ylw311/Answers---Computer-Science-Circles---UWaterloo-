n1 = input()
n2 = input()

n1i = int(n1)
n2i = int(n2)

fn = n1i % n2i

if fn == 0:
    print("divisible")
else:
    print("not divisible")
