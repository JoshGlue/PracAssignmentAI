class train

	def ExtractVocabulary(dataset):
		#Herleid de volledige vocubulary van alle woorden die voorkomen in de dataset
		return vocubulary

	def TrainMultinomialNaiveBayes(classes, dataset):
		# De specificatie van Probabilistic Inference and Bayesian Classification (Blz. 19) van Rieks op den Akker
		# moet hier geimplementeerd worden
		return [vocubulary, prior, condprob]


	def CountNumberOfDocs(dataset):
		# Telt het aantal documenten in de gehele dataset
		return N

	def CountDocsInClass(dataset, class):
		# Telt het aantal documenten in een klasse
		return NinClass

	def CountTokensOfTerm(concatenatedText, term):
		# Telt hoe vaak een woord voorkomt in de samengevoegde tekst.
		return tct

	def ConcatenateAllTextsOfDocsInClass(dataset, class):
		# Voegt alle tekst van alle documenten in een klasse samen
		return  concatenatedText