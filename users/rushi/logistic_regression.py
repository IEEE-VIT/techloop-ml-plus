from numpy import *

#training set
x = np.array([45,23,31,21,20,21,24,22,31,41,26,21,33,38,16,27,28,45,17,45])
y = np.array([1,1,0,1,1,1,0,0,0,0,0,1,0,0,1,1,0,1,1,1])

# ages of people under 50 yesrs having cancer
# 1 = yes; 0 = nope

learn = 0.00001

def sigmoid():
    sig = 1 / (1 + np.exp(-(z)))
    return sig

def trainer ():
    intercept1 = 0
    intercept2 = 0
    grad1 = 0
    grad2 = 0
    for i in range(len(y)):
        for j in range(len(x)):
            grad1 = (grad1 + (sigmoid(intercept1 + intercept2*x[j]) - y[i]))
            grad2 = (grad2 + (sigmoid(intercept1 + intercept2*x[j]) - y[i])*x[j])




