import rectangledata as gen
import matplotlib.pyplot as plt
import numpy as np
import random
import math
import time
import csv


def bruteForceApproach(dataset):
    resultsList = []

    for i in range(len(dataset)):
        resultsTemp = []
        count = 0
        for j in range(len(dataset)):
            if (i!=j) and (dataset[i][3]==dataset[j][1]) and (dataset[i][4] > dataset[j][2] and dataset[i][1] < dataset[j][4]):
                resultsTemp.append(j)
                resultsTemp.append(dataset[i][1])
                resultsTemp.append(dataset[j][2])
                resultsTemp.append(dataset[j][4])
                count +=1
        resultsTemp.insert(0, count)
        resultsTemp.insert(0, i)
        resultsList.append(resultsTemp)

    return resultsList

if __name__ == '__main__':

    stepSize = 5000
    step = 25
    maxSample = stepSize * step +1
    adjacenciesList = []
    rectanglesList = []

    with open('timings.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['input', 'time'])

        for sampleSize in range (stepSize, maxSample+1, stepSize):
            dataset = gen.generateData(sampleSize)

            start_time = time.time_ns() // 1000000
            result = (bruteForceApproach(dataset))
            end_time = time.time_ns() // 1000000

            running_time = end_time - start_time
            writer.writerow([len(dataset), running_time])

            rectanglesList.append(dataset)
            adjacenciesList.append(result)

    with open('adjacencies.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Adjacencies listed in format instructed'])

        for i in range(len(adjacenciesList)):
            writer.writerow(['Input Size', stepSize*i])
            writer.writerow(adjacenciesList[i])

    with open('rectangles.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Rectangles listed in format instructed (excluding index)'])

        for i in range(len(rectanglesList)):
            writer.writerow(['Input Size(correlates with number of rectangles)', stepSize*i])
            writer.writerow(rectanglesList[i])
