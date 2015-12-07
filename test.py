import classify.classfier as clas
import time
class tester:
    @staticmethod
    def TimeMeasure(classes ,vocubulary, prior, condprob, document):
        # Neemt een tijdmeting voor en na het uitvoeren van ApplyMultinomialNBC om te kijken
        # hoelang het duurt om deze uit te voeren op het gegeven document.
        start = time.time()
        classify.classifier.ApplyMultinomialNaiveBayes(classes ,vocubulary, prior, condprob, document)
        end = time.time()
        return end-start

    @staticmethod
    def Accuracy(classes ,vocubulary, prior, condprob, documents):
        # Voert ApplyMulitnomialNBC uit op een serie documenten, waarvan we de class kennen.
        # Er wordt geteld hoevaak de voorspelling overeenkomt met de echte waarde.
        # De teruggegeven waarde is een fractie tussen 0 en 1 die aangeeft welk deel van de keren de voorspelling correct was.
        correct = 0
        for d in documents:
            [topClass, score] = clas.ApplyMultinomialNaiveBayes(classes ,vocubulary, prior, condprob, d)       
            # wat is de exacte code voor de goede class eigenlijk?
            if topClass == :
                correct += 1
        return correct/len(documents)
