from data import Data
from train import Train
from classify import Classify
from test import Test
from Tkinter import *

class Application(Frame):

    def data(self):
        print "Creating Train File..."
        Data.CreateDataFile("train", "train.txt")
        print "Initializing Train File..."
        trainingSet = Data.LoadFile("train.txt")
        print "Creating Test File..."
        Data.CreateDataFile("test", "test.txt")
        print "Initializing Test File..."
        testSet = Data.LoadFile("test.txt")
        print "Extracting Classes.."
        classes = Train.ExtractClasses(trainingSet)

    def train(self):
        print "Training NBC..."
        vocabulary, prior, condprob = Train.TrainMultinomialNaiveBayes(classes, trainingSet)

    def speed(self):
        testDocument = Data.GetDocument(testSet)
        print "The time is took to do a single application of the NBC on a document is", Test.TimeMeasure(classes, vocabulary, prior, condprob, testDocument), "seconds."
        
    def accuracyOnTrain(self):
        percentage = Test.Accuracy(classes ,vocabulary, prior, condprob, dataSet)
        print "The percentage of correct predictions is ",100*percentage,"percent."

    def accuracyOnTest(self):
        percentage = Test.Accuracy(classes ,vocabulary, prior, condprob, testSet)
        print "The percentage of correct predictions is ",100*percentage,"percent."
        
    def switchToType(self,switchTo):
        if switchTo == 0:
            checkVarValues = [1, 0, 0]
        elif switchTo == 1:
            checkVarValues = [0, 1, 0]
        else:
            checkVarValues = [0, 0, 1]
        print checkVarValues
        self.setCheckVar(checkVarValues)
        
    def setCheckVar(self,checkVarValues):
        self.CheckVar1.set(checkVarValues[0])
        self.CheckVar2.set(checkVarValues[1])
        self.CheckVar3.set(checkVarValues[2])
        
    def createWidgets(self):
        self.labelFrame = LabelFrame(root,width=600,height=150, text="Enter Type:")
        self.labelFrame.grid_propagate(False)
        self.labelFrame.grid(row=1, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

        Checkbutton(self.labelFrame,text="E-mails",variable=self.CheckVar1,invoke=self.switchToType(0)).grid(row=0, column=0,sticky="W")
        Checkbutton(self.labelFrame,text="Blogs"  ,variable=self.CheckVar2,command=self.switchToType(1)).grid(row=1, column=0,sticky="W")
        Checkbutton(self.labelFrame,text="Jokes"  ,variable=self.CheckVar3,command=self.switchToType(2)).grid(row=2, column=0,sticky="W")

        self.labelFrame2 = LabelFrame(root,width=600,height=150, text="Operations:")
        self.labelFrame2.grid_propagate(False)
        self.labelFrame2.grid(row=4, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

        Button(self.labelFrame2, text="Gather Data", command=self.data())
        Button(self.labelFrame2, text="Train", command=self.train())
        Button(self.labelFrame2, text="Train", command=self.speed())
        Button(self.labelFrame2, text="Train", command=self.accuracyOnTrain)
        Button(self.labelFrame2, text="Train", command=self.accuracyOnTest)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid_propagate(False)
        self.grid()
        '''
        Variable boxes
        '''        
        self.CheckVar1 = IntVar()
        self.CheckVar2 = IntVar()
        self.CheckVar3 = IntVar()
        '''
        Variable boxes default values
        '''
        self.CheckVar1.set(1)
        self.CheckVar2.set(0)
        self.CheckVar3.set(0)
        '''
        Initializing step
        '''
        self.createWidgets()
        
root = Tk()
root.title("Multinomal Naive Bayesian Classifier")
root.geometry(("925x370"))
app = Application(master=root)
app.mainloop()

    