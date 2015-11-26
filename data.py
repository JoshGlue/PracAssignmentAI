class data
	

	def LoadFile(filename):
		#Pakt het tekstbestand en zet deze om naar een geschikte dataset
		#Het formaat waarin de documenten gespecificeerd worden in het tekstbestand is als volgt: {documentnaam} {klassenaam}
		#De inhoud van een tekstbestand kan er als volgt uitzien bij bijvoorbeeld een blog:
		#blogs/F/F-test1.txt F
		return dataset

	def PrepareTrainTestSet(dataset, ratio):
		#Pakt de dataset en split deze op in traindata en testdata naar de ratio die gespecificeerd is.
		normalize(dataset)
		return [trainingSet, testSet]

	def ExtractClasses(dataset):
		#Herleid alle mogelijke klasses die in de dataset voorkomen.
		return classes


	def Normalize(dataset):
		#Haalt alle interpunctie en hoofdletters weg
		#Voorbeeld: Hello, everyone. Do you like the new layout?
		#wordt: [hello, everyone, do, you, like, the, new, layout]
		return normalizedDataset

	def GetDocument(dataset):
		#Pakt een willekeurige document uit de dataset.
		return document









