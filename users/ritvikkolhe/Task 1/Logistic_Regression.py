import numpy as np
import math
import matplotlib.pyplot as plt

x=np.array([10,1,5,6,2,4,6,3,7,6,0,4,2,3,6,4,5,9,1,2,8,7]) #Hours studied
y=np.array([1,0,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0,1,0,1,1,1]) #Pass=1 and Fail=0

plt.scatter(x,y,color="r",marker="*",s=100)

W=0
B=0
alpha = 0.01

def Sigmoid(z):
    G_Z = float(1.0 / float((1.0 + math.exp(-1.0*z))))
    return G_Z
    
def Gradient_Descent(a,b,x,y,hours):
    for i in range(10000):
        gradient1=0
        gradient2=0
        for j in range(len(x)):
            gradient1+=((Sigmoid(a+(b*x[j]))-y[j]))
            gradient2+=((Sigmoid(a+(b*x[j]))-y[j])*x[j])
        a-=(alpha*gradient1)
        b-=(alpha*gradient2)
    return a,b,Sigmoid((b*hours)+a)

def graph(a,b):
    y=[]
    x=np.array(range(0,12))
    for i in x:
        y.append(Sigmoid(b*i+a))
    plt.plot(x,y)
    plt.show()

hr=int(input('Enter no. of hours studied: '))
W,B,percentage=Gradient_Descent(W,B,x,y,hr)
print('\nThere is '+str(round(percentage*100,2))+'% chance that you will pass in the exam.')

graph(W,B)
