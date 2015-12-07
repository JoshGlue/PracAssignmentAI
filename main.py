from data import Data
from train import Train
class main:

	def main():
		filename = 'dataset.txt'
		dataset = Data.LoadFile(filename)
		classes = Train.ExtractClasses(dataset)
		vocubulary, prior, condprob = Train.TrainMultinomialNaiveBayes(classes, trainingSet)
		testDocument = Data.getDocument(testSet)
		topClass, score = classify.ApplyMultinomialNaiveBayes(classes, vocubulary, prior, condprob, testDocument)
		print("{0} belongs to {1} with a score of {2}").format(testDocument, topClass, score )


	main()