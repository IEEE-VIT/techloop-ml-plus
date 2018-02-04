import numpy as np 
#Import data
x = np.array([17,23,31,21,20,21,24,22,31,41,26,21,33,38,16,27,28,17,17]) #Temperature in Celcius [INPUT]
y = np.array([1,1,0,1,1,1,0,0,0,0,0,1,0,0,1,1,0,1,1]) # 1 = It rained ; 0 = it didn't rain [ OUTPUT]

#Sigmoid Function
def sig(z):
    return 1 / (1 + np.exp(-(z)))

learning_rate = 0.0001

def gradientDes(x,y,val):  #Val is the value of Temperature in celcius for which we have to determine if it rained or no
    t1 = 0
    t2 = 0
    for i in range(10000):
        gradient1 = 0
        gradient2 = 0
        for j in range(len(x)):
            gradient1 = gradient1 + ((sig(t1+(t2*x[j])) - y[j]))
            gradient2 = gradient2 + ((sig(t1+(t2*x[j])) - y[j]) * x[j] )
        t1 = t1 - (learning_rate * gradient1)
        t2 = t2 - (learning_rate * gradient2)
    return sig(t1 + (t2 * val))

a = int(input('Enter the temperature in celcius: '))
print('There is a '+str(round(gradientDes(x,y,a)*100))+ '% chance that it will rain')