from data import Data

class Train:
	@staticmethod
	def ExtractVocabulary(dataset):
		#Herleid de volledige vocabulary van alle woorden die voorkomen in de dataset

		vocabulary = []
		for c in dataset:
			for d in dataset[c]:
				vocabulary.extend(dataset[c][d])
		vocabulary = set(vocabulary)
		return vocabulary

	@staticmethod
	def TrainMultinomialNaiveBayes(classes, dataset):
		# De specificatie van Probabilistic Inference and Bayesian Classification (Blz. 19) van Rieks op den Akker
		# moet hier geimplementeerd worden

		vocabulary = Train.ExtractVocabulary(dataset)
		numberofDocs = Train.CountNumberOfDocs(dataset)
		prior = {}
		condprob = {}
		for c in classes:
			print "Training Class", c
			nDocsInClass = Train.CountDocsInClass(dataset, c)
			prior[c] = nDocsInClass/numberofDocs
			concText = Train.ConcatenateAllTextsOfDocsInClass(dataset, c)
			nTokens2 = 0
			print "Calculating nTokens2"
			for t2 in vocabulary:
					nTokens2 += Train.CountTokensOfTerm(concText, t2)
			print "Calculating nTokens"
			for t in vocabulary:
				nTokens = Train.CountTokensOfTerm(concText, t)
				condprob[t][c] = (nTokens + 1)/(nTokens2 + 1)
				print "condprob", t, c, ": ", condprob[t][c]

		return [vocabulary, prior, condprob]

	@staticmethod
	def ExtractClasses(dataset):
		#Herleid alle mogelijke klasses die in de dataset voorkomen.
		return dataset.keys()

	
	@staticmethod
	def CountNumberOfDocs(dataset):
	# Telt het aantal documenten in de gehele dataset
		N = 0
		for C in dataset:
			N += Train.CountDocsInClass(dataset, C)			
		return N

	@staticmethod
	def CountDocsInClass(dataset, c):
		# Telt het aantal documenten in een klasse
		return  len(dataset[c])

	@staticmethod
	def CountTokensOfTerm(concatenatedText, term):
		# Telt hoe vaak een woord voorkomt in de samengevoegde tekst.
		return concatenatedText.count(term)

	@staticmethod
	def ConcatenateAllTextsOfDocsInClass(dataset, c):
		# Voegt alle tekst van alle documenten in een klasse samen
		concatenatedText = []
		for d in dataset[c]:
			concatenatedText.extend(dataset[c][d])
		return concatenatedText