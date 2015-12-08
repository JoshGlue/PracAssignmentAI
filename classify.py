import math
class Classify:
        @staticmethod
        def ApplyMultinomialNaiveBayes(classes ,vocabulary, prior, condprob, document):
        # De specificatie van Probabilistic Inference and Bayesian Classification (Blz. 20) van Rieks op den Akker
        # moet hier geimplementeerd worden
            score = {}
            W = Classify.ExtractTokensFromDoc(vocabulary, document)
            for c in classes:
                score[c] = math.log(prior[c],2)
                for t in W:
                    score[c] += math.log(condprob[t][c],2)
            topClass = max(score.keys(), key=(lambda k: score[k]))
            return [topClass,score[topClass]]

        @staticmethod
        def ExtractTokensFromDoc(vocabulary, document):
                # Geeft alle woorden terug die in het documenet voorkomt
                W = [word for word in document if word in vocabulary]                
                return set(W)

#def main():
#        print classifier.ExtractTokensFromDoc()
#main()
