pay = max(balance*0.021,10)
fpay = min(pay, balance)
print(fpay)


#------------or
print(min(balance, max(10,balance*0.021)))
