#This script was written for Math301 and it finds the Euler totient of argv[1]
#argv[1] expressions adcepted
import sys
import math

def ET(x):
    x = int(eval(x))
    card=0
    for y in range(1, x+1):
        if((math.gcd(x, y))==1):
            card+=1
    return card

upper = int(eval(sys.argv[1]))

lower = upper
if(len(sys.argv)==3):
    
    upper = int(eval(sys.argv[2]))
    lower = int(eval(sys.argv[1]))
if(upper<lower):
    temp=upper
    upper=lower
    lower=temp

out=[]
for x in range(lower, upper+1):
    card=0
    for y in range(1, x+1):
        if(math.gcd(x, y)==1):
            card+=1
    print("ET("+str(x)+")="+str(card))
    
