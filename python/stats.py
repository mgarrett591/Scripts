import sys
import math
#TODO
#Check the minus one
#pth Percentile

data=[]
dataTwo=[]
dataTwo=[]
if(len(sys.argv)==2):
	inflow=sys.argv[1].split(",")
	for x in inflow:
		data.append(float(x))
		dataTwo.append(float(x))
		
else:
	inflow=sys.argv[1].split(",")
	inflowTwo=sys.argv[2].split(",")
	for x in range(0,len(inflow)):
		data.append(float(inflow[x]))
		if(len(inflow)==len(inflowTwo)):
			dataTwo.append(float(inflowTwo[x]))
		dataTwo.append(float(inflow[x]))
	
def median(data):
	data=sorted(data)
	if(len(data)%2==1):
		return data[int((len(data)-1)/2)]
	else:
		return (data[int(len(data)/2)]+data[int((len(data)/2)+1)])/2

def relativeFreq(data, targetVal):
	freq=0
	for x in data:
		if(x==targetVal):
			freq+=1
	return freq/len(data)

def ApproxClassWidth(data, numberOfClasses):
	
	return (min(data)-max(data))/len(data)

def sampleMean(data):
	return sum(data)/(len(data)-1)

def mean(data):
	return sum(data)/len(data)

def weightedMean(data, weights):
	return 0
	#top=0
	#bottom=sum(weights)
	#max=len(weights)
	
	#for x in range(0,len(data)):
	#	top+=weights[x]*data[x]
	#return top/botton

def geometricMean(data):
	Cpi=1
	for x in data:
		Cpi=Cpi*x
	return Cpi**(1/len(data))
	
def locationOfPthPercentile(data, p):
	return p/100*(len(data)+1)
	
def pThPercentile(data, p):
	loc=locationOfPthPercentile(data, p)
	if(loc%1==0):
		return data[int(loc)]
	else:
		nDown=data[int(math.floor(loc))]
		if(len(data)>math.ceil(loc)):
			nUp=data[int(math.ceil(loc))]
		else:
			nUp=nDown
		frac=loc-math.floor(loc)
		return nDown+frac*(nUp-nDown)

def qOne(data):
	return pThPercentile(data, 25)
	
def qTwo(data):
	return pThPercentile(data, 50)
	
def qThree(data):
	return pThPercentile(data, 75)

def range(data):
	return max(data)-min(data)

def interquartileRange(data):
	return qOne(data)-qTwo(data)

def variance(data):
	Mean=mean(data)
	sum=float(0)
	for x in data:
		sum+=(x-Mean)**2
	return sum/len(data)

def sampleVariance(data):
	Mean=mean(data)
	sum=0
	for x in data:
		sum+=(x-Mean)**2
	return sum/(len(data)-1)

def std(data):
	return math.sqrt(variance(data))
	
def sampleStd(data):	
	return math.sqrt(sampleVariance(data))
	
def coefficientOfVariation(data):
	return (std(data)/mean(data))*100 
	
def sampleCoefficientOfVariation(data):
	return (std(data)/mean(data))*100 
	
def zScore(data, i):
	return (data[i-1]-mean(data))/std(data)

def zScoreVal(data, val):
	return (val-mean(data))/std(data)
	
def sampleZScore(data):
	return (data[i-1]-sampleMean(data))/sampleStd(data)
	
def covariance(data, dataTwo):
	sum=0
	x=0
	while(x<len(data)-2):
		sum+=(data[x]-mean(data))*(dataTwo[x]-mean(dataTwo))
		x+=1
	return sum/len(data)
	
def sampleCovariance(data,dataTwo):
	sum=0
	x=0
	while(x<len(data)-2):
		sum+=(data[x]-sampleMean(data))*(dataTwo[x]-sampleMean(dataTwo))
		x+=1
	return sum/(len(data)-1)

def PPMC(data, dataTwo):
	return covariance(data, dataTwo)/(variance(data)*variance(data))

def PPMCsample(data, dataTwo):
	return sampleCovariance(data, dataTwo)/(sampleVariance(data)*sampleVariance(data)) 



import sys
import math

targetVal=1
numberOfClasses=1
weights=[]
while(len(weights)!=len(data)):
	weights.append(1/len(data))
p=0
i=0

print("mean:","{0:.5f}".format(mean(data)))
print("median:","{0:.5f}".format(median(data)))
print("relativeFreq:","{0:.5f}".format(relativeFreq(data, targetVal)))
print("ApproxClassWidth:","{0:.5f}".format(ApproxClassWidth(data, numberOfClasses)))
print("sampleMean:","{0:.5f}".format(sampleMean(data)))
print("weightedMean:","{0:.5f}".format(weightedMean(data, weights)))
print("geometricMean:","{0:.5f}".format(geometricMean(data)))
print("locationOfPthPercentile:","{0:.5f}".format(locationOfPthPercentile(data, p)))
print("pThPercentile:","{0:.5f}".format(pThPercentile(data, p)))
print("qOne:","{0:.5f}".format(qOne(data)))
print("qTwo:","{0:.5f}".format(qTwo(data)))
print("qThree:","{0:.5f}".format(qThree(data)))
print("range:","{0:.5f}".format(range(data)))
print("interquartileRange:","{0:.5f}".format(interquartileRange(data)))
print("variance:","{0:.5f}".format(variance(data)))
print("sampleVariance:","{0:.5f}".format(sampleVariance(data)))
print("std:","{0:.5f}".format(std(data)))
print("sampleStd:","{0:.5f}".format(sampleStd(data)))
print("coefficientOfVariation:","{0:.5f}".format(coefficientOfVariation(data)))
print("sampleCoefficientOfVariation:","{0:.5f}".format(sampleCoefficientOfVariation(data)))
print("zScore:","{0:.5f}".format(zScore(data, i)))
print("sampleZScore:","{0:.5f}".format(sampleZScore(data)))
print("covariance:","{0:.5f}".format(covariance(data, dataTwo)))
print("sampleCovariance:","{0:.5f}".format(sampleCovariance(data,dataTwo)))
print("PPMC:","{0:.5f}".format(PPMC(data, dataTwo)))
print("PPMCsample:","{0:.5f}".format(PPMCsample(data, dataTwo)))

if("-zs" in sys.argv):
	for x in data:
		print(x,"zScore:",zScoreVal(data,x))