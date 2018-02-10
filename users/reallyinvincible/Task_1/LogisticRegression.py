import numpy as np
import matplotlib.pyplot as plt

b0, b1 = 0, 0

def sigmoid(x):
    return round(1/(1 + np.exp(-x)), 5)

def train(age, status, alpha, iterations):
    global b0, b1
    for i in range(iterations):
        correction1 = 0
        correction2 = 0
        for j in range(len(age)):
            correction1 += (sigmoid(round(b0+(b1*age[j]), 5)) - status[j])
            correction2 += (sigmoid(round(b0+(b1*age[j]), 5)) - status[j]) * age[j]
        b0 = b0 - (alpha * correction1)
        b1 = b1 - (alpha * correction2)
        #Uncomment the next line to see how the machine is learning
        #print(b0, b1)

def data_acquire():
    file = open('titanic.csv')
    status, age = [], []
    status = []
    age = []
    for i in file:
        data = i.split(',')
        if(data[6] != '' and 'Pass' not in data[0]):
            status.append(int(data[1]))
            age.append(round(float(data[6])))
    return age, status

def predict():
    user = float(input('\nEnter your age to check your probability of survival on board Titanic\n'))
    print('There is ' + str(sigmoid(b0 + user * b1)*100) + '% chance of your survival on board Titanic')
    choice = input('\nWanna Try another prediction(Y/N)\n')
    if choice == 'Y':
        predict()
    else:
        quit()

if  __name__ == '__main__':
    print('Acquiring data')
    age, status = data_acquire()
    print('Data Acquisition Complete ')
    alpha = 0.00001
    #Uncomment to try your own values
    #alpha = float(input('\nEnter the learning rate\n'))
    iterations = 10000
    #iterations = int(input('\nEnter the number of time the model should be trained\n'))
    print('Training started')
    train(age, status, alpha, iterations)
    print('Training Complete')
    print('Get ready to predict')
    plt.plot([i for i in range(0, 50)], [sigmoid(b0 + b1 * i) for i in range(50)], color = 'r')

    plt.show()
    predict()

