import numpy as np
## This logistic approach is used to determine the percentage possibility of rain on the factors such as temperature,wind speed and relative humidity

x1 = np.array([30,33,29,23,24,26,30,35,31,29,31,28,30,34]) ##temperature(in Celcius)
x2 = np.array([11,12,10,14,8,9,11,9,10,11,12,14,13,10]) ##wind speed(in km/h)
x3 = np.array([63,60,67,75,72,80,89,79,60,65,70,85,88,75])## relative humidity (in percentage)
n=len(x1)
y = np.array([0,0,1,1,1,1,1,0,0,1,0,1,0,0]) ## 1 depicts it rained,0 depicts it didn't

def sigmoid(x):
    return 1/(1+np.exp(-x))

m1=12
m2=12
m3=12
c=12
learning_rate = 0.001
p=int(input('Enter temperature in Celcius :-  '))
q=int(input('Enter wind speed in km/h :-  '))
r=int(input('relative humidity in percentage :-  '))



def gradient_descent(m1,m2,m3,c):
    for i in range(10000):
        c_gradient=0
        m1_gradient=0
        m2_gradient=0
        m3_gradient=0
        for j in range(n):
            c_gradient += (sigmoid(m1*x1[j]+m2*x2[j]+m3*x3[j]) - y[j])
            m1_gradient += (sigmoid(m1*x1[j]+m2*x2[j]+m3*x3[j]) - y[j])*x1[j]
            m2_gradient += (sigmoid(m1*x1[j]+m2*x2[j]+m3*x3[j]) - y[j])*x2[j]
            m3_gradient += (sigmoid(m1*x1[j]+m2*x2[j]+m3*x3[j]) - y[j])*x3[j]
        c -= learning_rate*c_gradient
        m1 -= learning_rate*m1_gradient
        m2 -= learning_rate*m2_gradient
        m3 -= learning_rate*m3_gradient
    return m1,m2,m3,c

m1,m2,m3,c=gradient_descent(m1,m2,m3,c)

def expect_value(p,q,r):
    y1=sigmoid(m1*p+m2*q+m3*r+c)
    return print('The percentage probabilty that it will rain is :-',y1*100)

expect_value(p,q,r)
