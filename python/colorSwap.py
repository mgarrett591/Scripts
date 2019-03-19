import numpy as np
from PIL import Image
import scipy.misc
import sys


#lets ask the user for some input
if(len(sys.argv) != 4 and len(sys.argv) != 5 and len(sys.argv) != 8 and len(sys.argv) != 11 and len(sys.argv) != 10 and len(sys.argv) != 14):
    print("python "+sys.argv[0]+" <fileName> ifRGB thenRGB")                                                   # (4 args) 
    print("python "+sys.argv[0]+" <fileName> ifRGB thenRGB elseRGB")                                           # (5 args)
    print("python "+sys.argv[0]+" <fileName> ifR ifG ifB thenR thenG thenB")                                   # (8 args)
    print("python "+sys.argv[0]+" <fileName> ifR ifG ifB thenR thenG thenB elseR elseG elseB")                 # (11 args)
    print("python "+sys.argv[0]+" <fileName> ifR ifG ifB ifT thenR thenG thenB thenT")                         # (10 args)
    print("python "+sys.argv[0]+" <fileName> ifR ifG ifB ifT thenR thenG thenB thenT elseR elseB elseB elseT") # (14 args)
    print(len(sys.argv))
    sys.exit()

#load good images into memeory
img=Image.open(sys.argv[1])
img=np.float32(img)
gMask = ["=", "=", "=", "="]
ifMask = ["*", "*", "*", "*"]
thenMask = ["*", "*", "*", "*"]
elseMask = ["*", "*", "*", "*"]

def pix(ifmask, gmask, pix):
    for x in range(0, len(pix)):
        if(gmask[x]=="="):
            if(ifmask[x]!="*" and ifmask[x]!=pix[x]):
                return False
        elif(gmask[x]==">"):
            if(ifmask[x]!="*" and ifmask[x]>=pix[x]):
                return False
        elif(gmask[x]=="<"):
            if(ifmask[x]!="*" and ifmask[x]<=pix[x]):
                return False
    return True

print(len(sys.argv))
if(len(sys.argv)==4):
    ifMask[0] == sys.argv[2]
    ifMask[1] == sys.argv[2]
    ifMask[2] == sys.argv[2]
    thenMask[0] == sys.argv[3]
    thenMask[1] == sys.argv[3]
    thenMask[2] == sys.argv[3]
elif(len(sys.argv) == 5):
    ifMask[0] == sys.argv[2]
    ifMask[2] == sys.argv[2]
    ifMask[3] == sys.argv[2]
    thenMask[0] == sys.argv[3]
    thenMask[1] == sys.argv[3]
    thenMask[2] == sys.argv[3]
    elseMask[0] == sys.argv[4]
    elseMask[1] == sys.argv[4]
    elseMask[2] == sys.argv[4]
elif(len(sys.argv) == 8):
    ifMask[0] == sys.argv[2]
    ifMask[2] == sys.argv[3]
    ifMask[3] == sys.argv[4]
    thenMask[0] == sys.argv[5]
    thenMask[1] == sys.argv[6]
    thenMask[2] == sys.argv[7]
elif(len(sys.argv) == 11):
    ifMask[0] == sys.argv[2]
    ifMask[2] == sys.argv[3]
    ifMask[3] == sys.argv[4]
    thenMask[0] == sys.argv[5]
    thenMask[1] == sys.argv[6]
    thenMask[2] == sys.argv[7]
    elseMask[0] == sys.argv[8]
    elseMask[1] == sys.argv[9]
    elseMask[2] == sys.argv[10]
elif(len(sys.argv) == 10):
    ifMask[0] == sys.argv[2]
    ifMask[2] == sys.argv[3]
    ifMask[3] == sys.argv[4]
    ifMask[4] == sys.argv[5]
    thenMask[0] == sys.argv[6]
    thenMask[1] == sys.argv[7]
    thenMask[2] == sys.argv[8]
    thenMask[3] == sys.argv[9]
elif(len(sys.argv) == 14):
    ifMask[0] == sys.argv[2]
    ifMask[2] == sys.argv[3]
    ifMask[3] == sys.argv[4]
    ifMask[4] == sys.argv[5]
    thenMask[0] == sys.argv[6]
    thenMask[1] == sys.argv[7]
    thenMask[2] == sys.argv[8]
    thenMask[3] == sys.argv[9]
    elseMask[0] == sys.argv[10]
    elseMask[1] == sys.argv[11]
    elseMask[2] == sys.argv[12]
    elseMask[3] == sys.argv[13]


for x in range(0 ,4):
    if(len(ifMask[x]) >= 3):
        if(ifMask[x][0:2]=="lt"):
            gMask[x]="<"
            ifMask[x] = ifMask[x][2:]
        elif(ifMask[x][0:2] == "gt"):
            gMask[x] = ">"
            ifMask[x]= ifMask[x][2:]
            

for x in range(0, 4):
    if(ifMask[x].isdigit()):
        ifMask[x] = int(ifMask[x])
    if(thenMask[x].isdigit()):
        thenMask[x] = int(thenMask[x])

print("  if mask =",ifMask)
print("   g mask =",gMask)
print("then mask =",thenMask)
print("else mask =",elseMask)
sys.exit()
for row in range(0, len(img)):
    for col in range(0, len(img[row])):
        if(pix(ifMask, gMask, img[row][col])):
            #print(ifMask)
            #print(gMask)
            #print(img[row][col])
            #print(pix(ifMask, gMask, img[row][col]))
            red = img[row][col][0]
            green = img[row][col][1]
            blue = img[row][col][2]
            avrege = (red+green+blue)/3
            for x in range(0, 4):
                if(type(thenMask[x])==int):
                    img[row][col][x] = thenMask[x]
                elif(thenMask[x]=="r"):
                    img[row][col][x] = red
                elif(thenMask[x]=="g"):
                    img[row][col][x] = green
                elif(thenMask[x]=="b"):
                    img[row][col][x] = blue
                elif(thenMask[x] == "a"):
                    img[row][col][x] = avrege
                elif(thenMask[x] == "-r"):
                    img[row][col][x] = 255-red
                elif(thenMask[x] == "-g"):
                    img[row][col][x] = 255-green
                elif(thenMask[x] == "-b"):
                    img[row][col][x] = 255-blue
                elif(thenMask[x] == "-a"):
                    img[row][col][x] = 255-avrege
                
                

            
            

scipy.misc.imsave('edited'+sys.argv[1], img)

