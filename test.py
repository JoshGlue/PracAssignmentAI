from classify import Classify
import time

class Test:
    @staticmethod
    def TimeMeasure(classes ,vocabulary, prior, condprob, document):
        # Neemt een tijdmeting voor en na het uitvoeren van ApplyMultinomialNBC om te kijken
        # hoelang het duurt om deze uit te voeren op het gegeven document.
        start = time.time()
        Classify.ApplyMultinomialNaiveBayes(classes ,vocabulary, prior, condprob, document)
        end = time.time()
        return end-start

    @staticmethod
    def Accuracy(classes ,vocabulary, prior, condprob, dataset):
        # Voert ApplyMulitnomialNBC uit op een serie documenten, waarvan we de class kennen.
        # Er wordt geteld hoevaak de voorspelling overeenkomt met de echte waarde.
        # De teruggegeven waarde is een fractie tussen 0 en 1 die aangeeft welk deel van de keren de voorspelling correct was.
        correct = 0
        for data in dataset.values():
            topClass, score = Classify.ApplyMultinomialNaiveBayes(classes ,vocabulary, prior, condprob, data[0])       
            if topClass == data[1]:
                correct += 1
        return correct/len(dataset)
