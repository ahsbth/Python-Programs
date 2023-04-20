import math
print('Enter the side of tringle=')
a=float(input())
b=float(input())
c=float(input())
s=float(a+b+c)/2
print(s)
s1=s*(s-a)*(s-b)*(s-c)
print(s1)
a=math.sqrt(s1)
print('area of traingle=',a)
