## e^x = 1+x/1!+x^2/2!+...x^n/n!+....
import math
x=float(input())
eps=float(input())

S=1
p=1
i=1
while eps<math.fabs(p):
       p=p*x/i
       S+=p
       i+=1

print(S)
