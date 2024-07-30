#password verifier
s=input()
n=len(s)
count=0
str="@/"
for i in s:
    if(i==str[0] or i==str[1] and i!=' '):
        count+=1
        break
if(count==0):
    print("please follow the conditions")
elif(n<8):
    print("please follow the conditions")
elif(n==8):
    print("password is weak")
elif(n>8 and n<12):
    print("password is moderate")
elif(n>12 and n<15):
    print("password is strong")
else:
    print("very strong")