import numpy as np
import matplotlib.pyplot as plt

x = np.array([17,23,31,21,20,21,24,22,31,41,26,21,33,38,16,27,28,17,17,21,23,32,26,16])
y = np.array([1,1,0,1,1,1,0,0,0,0,0,1,0,0,1,1,0,1,1,1,1,0,1,1])

w = 0
b = 0

def func(x,w,b):
    return (w*x+b)

def sigmoid (x,w,b):
    return(1/(1+ np.exp(-func(x,w,b))))

def gradient_descent (x,y,w,b,iterations,alpha,temp):
	for i in range (iterations):
		w_gradient = 0
		b_gradient = 0 
		for j in range (len(x)):
			b_gradient = b_gradient + alpha*((2*(sigmoid(x[j],w,b) - y[j]))/len(x))
			w_gradient = w_gradient + alpha*((2*((sigmoid(x[j],w,b) - y[j])*x[j]))/len(x))
		w = w - w_gradient
		b = b - b_gradient
	return sigmoid(temp,w,b)
   
temp = int(input("Enter the temp : "))

print("There is a ",str(round(gradient_descent(x,y,w,b,1000,0.001,temp)*100)),"% chance that it will rain")
