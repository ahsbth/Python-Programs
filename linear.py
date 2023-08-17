import numpy as np
n=input(print("Enter the no for search="))
a=[1,2,3,4,5,6,7,8]
f=0
for i in range(1,len(a)):
    if(a[i]==n):
        print("no is found")
        break
    else:
        print("no is not found")

   