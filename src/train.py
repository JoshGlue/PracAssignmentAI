from __future__ import division
from data import Data
from collections import Counter
import random
import time

class Train:
	@staticmethod
	def ExtractVocabulary(dataset):
		#Herleid de volledige vocabulary van alle woorden die voorkomen in de dataset

		vocabulary = []
		for c in dataset:
			for d in dataset[c]:
				vocabulary.extend(dataset[c][d])
		vocabulary = set(vocabulary)
		vocabulary = filter( lambda w :  len(w)>3 and len(w) <11, vocabulary)
		
		vocabulary = random.sample(vocabulary, int(len(vocabulary) * 0.4))
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
			start = time.time()
			print "Training Class", c
			nDocsInClass = Train.CountDocsInClass(dataset, c)
			prior[c] = nDocsInClass/numberofDocs
			concText = Train.ConcatenateAllTextsOfDocsInClass(dataset, c)
			T = len(concText)
			V = len(vocabulary)
			print "Length of vocabulary is", V, "Words"
			tempDict = Counter(concText)
			nTokens4 = dict(tempDict)
			print "Length of tempDict is", len(tempDict), "Key-Value Pairs"
			for k in tempDict:
				if k not in vocabulary:
					del nTokens4[k]
			print "Length of tokens4 is", len(nTokens4), "Key-Value Pairs"
			print "Calculating Condtional Probabilities"
			for t in vocabulary:
				if not t in condprob.keys():
					condprob[t] = {}
				condprob[t][c] = (nTokens4.get(t,0)+1)/(T+V)
#				print "condprob", t, c, ": ", condprob[t][c]
			print "Finished Training Class", c
			end = time.time()
			print "Training Class", c, "Took", end-start, "Seconds."
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
	def ConcatenateAllTextsOfDocsInClass(dataset, c):
		# Voegt alle tekst van alle documenten in een klasse samen
		concatenatedText = []
		for d in dataset[c]:
			concatenatedText.extend(dataset[c][d])
		return concatenatedText