import numpy as np

#Credit score range 300-850 on the basis of which you will get a loan 
g = np.array([500,720,690,300,370,632,820,425,740,430,421,323,620,519,620,530,422,616])
 #random initialization whether loan will be sanctioned
h = np.array([0,1,1,0,0,1,1,0,1,0,1,0,1,1,1,0,0,1])
def sigmoid(g):
    return 1/(1+np.exp(-g))
alpha=0.00001


def grad_decent(g,h,inpu):
    d1,d2=0,0
    for i in range(1000):
        grad1 = 0
        grad2 = 0
        for j in range(len(g)):
            grad1 += sigmoid(d1+d2*g[j]) - h[j]
            grad2 += (sigmoid(d1+d2*g[j]) - h[j])*g[j]
        d1 -= alpha*grad1
        d2 -= alpha*grad2
    return sigmoid(d1+d2*inpu)

inpu = int(input('Enter the credit score you have'))
print('probability of you getting getting the loan=  ' + str(grad_decent(g,h,inpu)))
