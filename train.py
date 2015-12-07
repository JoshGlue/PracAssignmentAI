from data import Data

class Train:
	@staticmethod
	def ExtractVocabulary(dataset):
		#Herleid de volledige vocubulary van alle woorden die voorkomen in de dataset

		vocubulary = []
		for c in dataset:
			for d in dataset[c]:
				vocubulary.extend(dataset[c][d])
		vocubulary = set(vocubulary)
		return vocubulary

	@staticmethod
	def TrainMultinomialNaiveBayes(classes, dataset):
		# De specificatie van Probabilistic Inference and Bayesian Classification (Blz. 19) van Rieks op den Akker
		# moet hier geimplementeerd worden

		vocubulary = ExtractVocabulary(dataset)
		numberofDocs = CountNumberOfDocs(dataset)
		prior = {}
		condprob = {}
		for c in classes:
			nDocsInClass = CountDocsInClass(dataset, c)
			prior[c] = nDocsInClass/numberofDocs
			concText = ConcatenateAllTextsOfDocsInClass(dataset, c)
			for t in vocubulary:
				nTokens = CountTokensOfTerm(concText, t)
				for t2 in vocubulary:
					nTokens2 += CountTokensOfTerm(conctext, t2)
				condprob[t][c] = (nTokens + 1)/(nTokens2 + 1) 

		return [vocubulary, prior, condprob]

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
def main():
	dataset =  Data.LoadFile('dataset.txt')
	print Train.ExtractClasses(dataset)
	print Train.CountNumberOfDocs(dataset)


main()