import math
n=int(input("Nechta kordinata kiritasiz:"))            

maxNumber=0

for i in range(1,n+1):
    
    ##Bu yerda x ning kordinatasi kiritiladi
    print("x[",i,"]ni kiriting:")
    x=int(input())
    
    ##Bu yerda y ning kordinatasi kiritiladi
    print("y[",i,"]ni kiriting:")
    y=int(input())
    
    if ((x**2+y**2)>maxNumber):
        maxNumber=(x**2+y**2)

print("Radiusi ",math.sqrt(maxNumber))
