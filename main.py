from data import Data
from train import Train
from classify import Classify
from test import Test
class main:

	def main():
		print "Creating Train File..."
		Data.CreateDataFile("train", "train.txt")
		print "Initializing Train File..."
		trainingSet = Data.LoadFile("train.txt")
		print "Creating Test File..."
		Data.CreateDataFile("test", "test.txt")
		print "Initializing Test File..."
		testSet = Data.LoadFile("test.txt")
		print "Extracting Classes.."
		classes = Train.ExtractClasses(trainingSet)
		print "Training NBC..."
		vocabulary, prior, condprob = Train.TrainMultinomialNaiveBayes(classes, trainingSet)
		print "Testing Accuracy..."
		percentage = Test.Accuracy(classes ,vocabulary, prior, condprob, testSet)
		print "The percentage of correct predictions is ",100*percentage,"percent."
		print "Get Random Document..."
		testDocument = Data.GetDocument(testSet)
		print "Do A Time Measurement of the Application of the NBC..."
		print "The time is took to do a single application of the NBC on a document is", Test.TimeMeasure(classes, vocabulary, prior, condprob, testDocument), "seconds."
		print "Applying NBC on Document..."
		topClass, score = Classify.ApplyMultinomialNaiveBayes(classes, vocabulary, prior, condprob, testDocument['document'])

	main()
