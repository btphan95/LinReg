#Lab 11
import math
import random
import numpy as np
intxt = open("Amazon.txt","r")
out = open("out.txt","w")
#Read data from in.txt
txt = intxt.read() 

txtlist = txt.split()
x = list()
y = list()

for i in range(1,len(txtlist)):
	if i%2==0:
   		x.append(txtlist[i])
   	else:
		y.append(txtlist[i])

z = zip(x, y)
random.shuffle(z)
x,y = zip(*z)

trainnum = int(0.8*float(len(x)))#choose 80% of data to train


#training data
xtrain = list()
ytrain = list()
index = list()
xtest = list()
ytest = list()
yr = list()

for i in range(len(x)):
	if i<trainnum:
 		xtrain.append(int(x[i]))
	 	ytrain.append(int(y[i]))
 	else:
 		xtest.append(int(x[i]))
 		ytest.append(int(y[i]))


xtrain = list(map(int,xtrain))
ytrain = list(map(int,ytrain))


polyr = np.polyfit(xtrain,ytrain,2)

totalerror = 0

for i in range(len(ytest)):
 	v = polyr[0]*xtest[i]**2 + polyr[1]*xtest[i] + polyr[2]
 	yr.append(v)
 	z = str(xtest[i]) + " " + str(ytest[i]) + " " +str(yr[i])
 	totalerror = totalerror + (int(y[i])-int(yr[i]))**2
 	
totalerror = totalerror/len(ytest)
rms = math.sqrt(totalerror) 
for i in range(5):
	newrms = math.sqrt(totalerror)
	if newrms < rms:
		rms = newrms
print("RMS: ", rms)


#testing data has x and y, xtest apply to the regression => approximated y 

#based on regression

#xtest, ytest

#you want to compare ytest and the approximated based regression

#sum up for all the test data: rms = "yest - yapprox)^^2"

#repeat the process at least twice, so you have two rms values (for two regression. pick the better of the two.)

#mention that in the readme.pdf

#Print regression

#Gives two coefficients representing a line
