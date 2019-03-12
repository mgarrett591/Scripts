import sys
import random
    
def dice(sides=6):
    
    print(random.randint(1, sides))

def loop(val):
    print('loop..')
    while((val=='')or(type(val)==type(int(1)))):
        val=input()
        dice(val)

if(len(sys.argv)>=2):
    if(dice=='m'):
        loop('')
    out=dice(int(sys.argv[1]))
else:
    dice()
