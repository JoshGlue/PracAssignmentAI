from data import Data
from train import Train
from classify import Classify
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
		print "Get Random Document..."
		testDocument = Data.getDocument(testSet)
		print "Applying NBC on Document..."
		topClass, score = Classify.ApplyMultinomialNaiveBayes(classes, vocabulary, prior, condprob, testDocument)
		print("{0} belongs to {1} with a score of {2}").format(testDocument, topClass, score )
		
	main()
