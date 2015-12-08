import re
import random
import os
class Data:

	@staticmethod
	def CreateDataFile(directory, file):
		with open(file, 'w+') as file_:
			for root, dirs, files in os.walk(directory):
				for file in files:					
					file_.write(os.path.join(root, file) + " " + os.path.basename(root) + "\n")


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

	#Geeft een dictionary terug met het document en de klasse
	#Waar het bij hoort
	@staticmethod
	def GetDocument(dataset):
		alldocuments = []
		for c in dataset:
			for d in dataset[c]:
				document = {}
				document['class'] = c
				document['document'] = dataset[c][d]
				alldocuments.append(document)
		index =random.randint(0, len(alldocuments) -1)
		return alldocuments[index]