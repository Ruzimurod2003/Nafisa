## x berilgan: max(ch(x),1+|x|,(1+x*x)^x) topish kerak
import math
x=float(input())

a=(math.exp(x)+math.exp(-x))/2
b=(math.fabs(x)+1)
c=(math.pow((1+(x*x)),x))

if a>b and a>c:
    if b>c:
        print(c,b,a)
    else:
        print(b,c,a)
elif b>a and b>c:
    if a>c:
        print(c,a,b)
    else:
        print(a,c,b)
elif c>a and c>b:
    if a>b:
        print(b,a,c)
    else:
        print(a,b,c)
