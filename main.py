# Example of Naive Bayes implemented from Scratch in Python
import csv
import random
import math

def loadCsv(filename):


def splitDataset(dataset, splitRatio):


def separateByClass(dataset):


def mean(numbers):


def stdev(numbers):


def summarize(dataset):


def summarizeByClass(dataset):


def calculateProbability(x, mean, stdev):


def calculateClassProbabilities(summaries, inputVector):

			
def predict(summaries, inputVector):


def getPredictions(summaries, testSet):


def getAccuracy(testSet, predictions):


def main():
	filename = 'pima-indians-diabetes.data.csv'
	splitRatio = 0.67
	dataset = loadCsv(filename)
	trainingSet, testSet = splitDataset(dataset, splitRatio)
	print('Split {0} rows into train={1} and test={2} rows').format(len(dataset), len(trainingSet), len(testSet))
	# prepare model
	summaries = summarizeByClass(trainingSet)
	# test model
	predictions = getPredictions(summaries, testSet)
	accuracy = getAccuracy(testSet, predictions)
	print('Accuracy: {0}%').format(accuracy)

main()