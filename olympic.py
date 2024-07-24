badh=int(input("height of x"))
badw=int(input("weight of x"))
tenh=int(input("height of y"))
tenw=int(input("weight of y"))
fact7=(50*14)/100
if(badh==140 and badw%2==0):
    print("Mr.X are selected for badminton")
elif(tenh<140 and tenh>118 and tenw%fact7==0):
    print("Mr.Y are selected for table tennis") 
else:
    print("Mr.Z are selected for swimming")