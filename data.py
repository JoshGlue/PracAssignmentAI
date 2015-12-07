import re
import random

class Data:

	@staticmethod
	def LoadFile(filename):
		#Pakt het tekstbestand en zet deze om naar een geschikte dataset
		#Het formaat waarin de documenten gespecificeerd worden in het tekstbestand is als volgt: {documentnaam} {klassenaam}
		#De inhoud van een tekstbestand kan er als volgt uitzien bij bijvoorbeeld een blog:
		#blogs/F/F-test1.txt F
		dataset = {}
		with open(filename) as f:
			for line in f:
				document = re.split(' ',line)
				documentFile = document[0]
				documentclass = document[1].strip()
				with open(documentFile) as d:					
					lines = d.read()
					bagOfWords = re.split(' ',lines)
					normalizedBagOfWords = Data.Normalize(bagOfWords)
					#Als de klasse not niet bestaat, maak hem aan
					if not documentclass in dataset.keys():
						dataset[documentclass] = {}
				    #Het document komt genormaliseerd in de dataset te staan
					dataset[documentclass][documentFile] = normalizedBagOfWords
		return dataset


	#### MOET NOG GEIMPLEMENTEERD WORDEN ####
	@staticmethod
	def PrepareTrainTestSet(dataset, ratio):
		#Pakt de dataset en split deze op in traindata en testdata naar de ratio die gespecificeerd is.


		return [trainingSet, testSet]


	@staticmethod
	def Normalize(document):
		#Haalt alle interpunctie en hoofdletters weg
		#Voorbeeld: Hello, everyone. Do you like the new layout?
		#wordt: [hello, everyone, do, you, like, the, new, layout]
		#Zet alle woorden om naar kleine letters
		normalizedDocument = [d.lower() for d in document]
		#Haal alle \n, \r's weg
		normalizedDocument = [d.strip() for d in normalizedDocument]		
		#Haal alle interpunctie weg
		normalizedDocument = [re.sub(r"[^a-z]", "", d) for d in normalizedDocument]
		#Haal alle items weg die leeg zijn
		normalizedDocument = filter(None, normalizedDocument)
		return normalizedDocument

	@staticmethod
	def GetDocument(dataset):
		#Pakt een willekeurige document uit de dataset.
		return document
def main():
		 dataset =  Data.LoadFile('dataset.txt')
		 print "hello"
		 print dataset
	



main()








