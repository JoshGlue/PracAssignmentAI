import train
import data
import classify

class main

	def main():
		filename = 'classifiedDocuments.txt'
		splitRatio = 0.67
		dataset = data.LoadFile(filename)
		trainingSet, testSet = data.PrepareTrainTestData(dataset, splitRatio)
		classes = data.ExtractClasses(dataset)
		vocubulary, prior, condprob = train.TrainMultinomialNaiveBayes(classes, trainingSet)
		testDocument = data.getDocument(testSet)
		topClass, score = classify.ApplyMultinomialNaiveBayes(classes, vocubulary, prior, condprob, testDocument)
		print("{0} belongs to {1} with a score of {2}").format(testDocument, topClass, score )


	main()