import math
print('Enter principle,rate and time=')
p=float(input())
r=float(input())
t=float(input())
A=p*(math.pow((1+r/100),t))
ci=A-p
print('Compund intreast=',ci)
