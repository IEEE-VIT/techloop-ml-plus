import numpy as np
##This linear approach is done in order to determine the marks scored in an exam on the factors such as hours studied, hours slept and hours played on a day.
x1= np.array([6,3,4,7,8,10,6,8,3,9])## hours studied
x2= np.array([6,7,4,6,9,5,5,6,8,6])## hours slept
x3= np.array([6,5,5,3,2,2,4,5,3,1])## hours played
y = np.array([90,91,70,75,80,89,93,77,79,86])## marks scored
n=len(x1)
m1= 12
m2= 12
m3= 12
c = 12

learning_rate= 0.001

p=int(input('Enter the number of hours studied in a day :- '))
q=int(input('Enter the number of hours slept in a day :-  '))
r=int(input('Enter the number of hours played in a day :- '))
if (p+q+r<24) : ##Since it Impossible to things more than 24 hours in a day
    def gradient_descent(m1,m2,m3,c):
        for i in range(10000):
            c_gradient = 0
            m1_gradient = 0
            m2_gradient = 0
            m3_gradient = 0
            for j in range(n):
                m1_gradient += 2*(m1*x1[j] +m2*x2[j] +m3*x3[j] + c - y[j])*x1[j]/n
                m2_gradient += 2*(m1*x1[j] +m2*x2[j] +m3*x3[j] + c - y[j])*x2[j]/n
                m3_gradient += 2*(m1*x1[j] +m2*x2[j] +m3*x3[j] + c - y[j])*x3[j]/n
                c_gradient += 2*(m1*x1[j] +m2*x2[j] +m3*x3[j] + c - y[j])/n
            m1 = m1 - (learning_rate * m1_gradient)
            m2 = m2 - (learning_rate * m2_gradient)
            m3 = m3 - (learning_rate * m3_gradient)
            c = c - (learning_rate * c_gradient)
        return m1,m2,m3,c


    m1,m2,m3,c = gradient_descent(m1,m2,m2,c)

    def expect_value (p,q,r):
        y1=m1*p+m2*q+m3*r+c
        if (y1>100): ## since marks scored cannot be greater than 100
            return ('Marks scored :- 100')
        else:
            return print('Marks scored :- ',y1)


    expect_value(p,q,r)

else:
    print('Impossible time distribution')
