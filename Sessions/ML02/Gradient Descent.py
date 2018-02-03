from numpy import *

# y = mx + bias
# weight is slope, bias is y-intercept
def computingError(bias, weight, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        totalError += (y - (weight * x + bias)) ** 2
    return totalError / float(len(points))

def gradientDescent(biadCurrent, weightCurrent, points, learningRate):
    biasGradient = 0
    weightGradient = 0
    N = float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        biasGradient += -(2/N) * (y - ((weightCurrent * x) + biadCurrent))
        weightGradient += -(2/N) * x * (y - ((weightCurrent * x) + biadCurrent))
    newBias = biadCurrent - (learningRate * biasGradient)
    newWeight = weightCurrent - (learningRate * weightGradient)
    return [newBias, newWeight]

def calculateWeightAndBias(points, startingBias, startingWeight, learning_rate, num_iterations):
    bias = startingBias
    weight = startingWeight
    for i in range(num_iterations):
        bias, weight = gradientDescent(bias, weight, array(points), learning_rate)
    return [bias, weight]

def run():
    # importing the dataset of marks
    points = genfromtxt("CAT.csv", delimiter=",")
    # change the learning rate value and see what happens to the wrror bias and weight
    learning_rate = 0.0001
    initialBias = 0
    initialWeight = 0
    num_iterations = 1000
    print("Starting gradient descent at bias = {0}, weight = {1}, error = {2}".format(initialBias, initialWeight, computingError(initialBias, initialWeight, points)))
    [bias, weight] = calculateWeightAndBias(points, initialBias, initialWeight, learning_rate, num_iterations)
        # printing the value of the results
    print("After {0} iterations bias = {1}, weight = {2}, error = {3}".format(num_iterations, bias, weight, computingError(bias, weight, points)))

if __name__ == '__main__':
    run()
