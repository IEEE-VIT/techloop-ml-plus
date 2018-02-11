# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:08:26 2018

@author: Srivatsan
LogReg using numpy
"""
from numpy import *
import matplotlib.pyplot as plt
alpha=0.001
l=w=c=0
itern=20000   
def hyplin(x,w,c):
    return (float(w*x+c))

def sigmoid(var,w,c):
    return float(1/(1+exp(-hyplin(var,w,c))))
    
def graddec(x, y, w, c,m, itern, alpha):
    for j in range(itern):
        for i in range(m):
            w=w- (alpha*(2/m)*(sigmoid(x[i],w,c)-y[i])*x[i])
            c=c- (alpha*(2/m)*(sigmoid(x[i],w,c)-y[i]))
    return [w, c]

def predict(w, c): #predicts output for given input after classification
    hours= float(input())
    t= sigmoid(hours,w,c)
    
    if t>=0.5:
        print ("Pass")
    else:
        print ("Fail")
    return t

points = genfromtxt("exam.csv", delimiter=",")
x= points[...,1]
y= points[...,2]
m=len(x)
[w, c]= graddec(x, y,w,c,m, itern, alpha)
t=predict(w,c)
print(w,c, t) #Prints values of theta0, theta1 and preticted probability
t=[t for i in range(m)]
x1=arange(len(t))
plt.plot(x1,t)
plt.scatter(x, y, color = "m", marker = "o", s = 30)
plt.xlabel("Number of hours of study")
plt.ylabel("Probability of pass")
plt.show()
