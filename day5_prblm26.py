vowel="aeiou"
con="bcdfghklmnpqrstvwxyz"
sp=' '
s=input()
sum=0
for i in s:
    if(i not in vowel and i not in con and i not in sp):
        #if(i.isnumeric):
        sum+=1
print(sum)