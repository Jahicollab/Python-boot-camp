apples=int(input("no. of apples:"))
bananas=int(input("no. of bananas:"))
oranges=int(input("no. of oranges:"))
costa=int(15)
costb=int(4)
costo=int(5)
given=int(input("given money"))
ta=apples*costa
tb=bananas*costb*12
to=oranges*costo
sum=ta+tb+to
print(sum)
print(given-sum)
if(sum<=given):
   print("not cheated")
else:
   print("cheated")    
