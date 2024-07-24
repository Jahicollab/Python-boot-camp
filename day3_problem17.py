##find sum of squares of in a given number 
n=int(input())
sum=0
while(n>0):
    r=n%10
    sum+=r*r    #sum+=r**2
    n=n//10
print("sum of the squares of each digit in a number:",sum)