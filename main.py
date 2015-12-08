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
#		percentage = Test.Accuracy(classes ,vocabulary, prior, condprob, trainingSet)
		#print "The percentage of correct predictions is ",percentage,"percent."
		print "Get Random Document..."
		testDocument = Data.GetDocument(testSet)
		print "Do A Time Measurement of the Application of the NBC..."
		print Test.TimeMeasure(classes, vocabulary, prior, condprob, testDocument)
		print "Applying NBC on Document..."
		topClass, score = Classify.ApplyMultinomialNaiveBayes(classes, vocabulary, prior, condprob, testDocument['document'])
		print("{0} belongs to {1} with a score of {2}").format(testDocument, topClass, score )

	main()
