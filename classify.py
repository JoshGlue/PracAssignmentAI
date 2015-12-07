import math
import numpy
class Classify:
        @staticmethod
        def ApplyMultinomialNaiveBayes(classes ,vocubulary, prior, condprob, document):
        # De specificatie van Probabilistic Inference and Bayesian Classification (Blz. 20) van Rieks op den Akker
        # moet hier geimplementeerd worden
                W = ExtractTokensFromDoc(vocubulary, document)
                for c in classes:
                        score[c] = math.log(prior[c])
                        for t in W:
                                score[c] += math.log(condprob[t][c])
                topClass = numpy.argmax(score)
                return [topClass,score[topClass]]

        @staticmethod
        def ExtractTokensFromDoc(vocabulary, document):
                # Geeft alle woorden terug die in het documenet voorkomt
                W = [word for word in document if word in vocubulary]                
                return set(W)

#def main():
#        print classifier.ExtractTokensFromDoc()
#main()
