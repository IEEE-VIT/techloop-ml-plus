import numpy as np
import matplotlib.pyplot as plt

x= np.array([1,2,3,5,8,9,11,12])    
y= np.array([0,0,0,1,1,0,1,1])

def sigmoid(z):                        
    return 1/(1+np.exp(-z))

a[i]= sigmoid(W*x[i]+B)

def loss(a,y):
    error=0
    for i in range(len(x)):
        temp= -(y[i]*(loga[i])+(1-y[i])*log(1-a[i]))
        error+=temp
    return error/float(len(x))


def gradient(x,y,iterations,alpha,val):
    W=0
    B=0
    for i in range(iterations):
        B_gradient=0
        W_gradient=0
        for j in range(len(x)):
            B_gradient += (a[j]-y[j])/len(x)
            W_gradient += ((a[j]-y[j])*x[j])/len(x)
        W= W- alpha*W_gradient
        B= B- alpha*B_gradient
    return W,B

alpha= 0.001
iterations= 10000
W2,B2= gradient(x,y,10000,0.001,val)

def probability(val):
    a= sigmoid(W2*val+B2)
    
value=int(input('Enter the value:'))
print( " the probability is" + probability(value))
        
        
        
