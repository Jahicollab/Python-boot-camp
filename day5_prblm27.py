vowel="aeiou"
con="bcdfghjklmnpqrstvwxyz"
ct_c=0
ct_v=0
s=input()
new=s.lower()
for i in new:
    if(i in vowel):
        ct_v+=1
for i in new:
    if(i in con):
        ct_c+=1
print("the vowel count of the given string is:",ct_v)
print("the consonant count of the given string is:",ct_c)
