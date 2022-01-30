## e^x = 1+x/1!+x^2/2!+...x^n/n!+....
import math


###1-ko'rinishi
x=int(input())
n=100
S=1
p=1
for i in range(1,n):
       p=p*x/i
       S+=p
       
print(S)



###2-ko'rinishi
def exponential(n, x):
    sum = 1.0
    for i in range(n, 0, -1):
        sum = 1 + x * sum / i
    print (sum)

exponential(n, x)


###3-ko'rinishi
print(math.exp(x))

###4-ko'rinishi
print(math.pow(math.e,x))

###5-ko'rinishi
while i<n:
       p=p*x/i
       S+=p
       i+=1
print(S)

input()
