age=int(input("enter the age of the person"))
if(age>=18 and age<24):
  print("only 2 wheeler")
elif(age>=24 and age<45):
  print("two and four wheeler only")
elif(age>45):
  print("all")
else:
  print("can not drive")  
  