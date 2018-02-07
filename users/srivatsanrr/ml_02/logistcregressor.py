# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 11:08:26 2018

@author: Srivatsan
LogReg using numpy and matplotlib
"""
import numpy as np
import matplotlib as plt

alpha=0.001
l=m=c=0
itern=1000
features=[200, 3]
weights=[3,1]
pred=[200, 1]
    
def ohypf(x):
    retrn(m*x+c)

def costfn():
    for i in range(len(x)):
        J+= (1/N)*(hypf(x(i))-y(i))**2

def sigmoid(var):
    return (1/(1+np.exp(-var)))

def predict(features, weights):
    z= np.dot(features, weights)
    return sigmoid(z)
def costfunctionfeatures, labels, weights():
    

def initw()
        

def cfn(x):
    for i in range(1,m+1):
        l+=y(i)*log(h(x(i)))+(1-y(i))*log(1-h(x(i)))
    
points = genfromtxt("dn.csv", delimiter=",")
x=points[:,1]
[m, c]= graddec