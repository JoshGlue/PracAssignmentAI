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
        self.trainingSet = Data.LoadFile("train.txt")
        print "Creating Test File..."
        Data.CreateDataFile("test", "test.txt")
        print "Initializing Test File..."
        self.testSet = Data.LoadFile("test.txt")
        print "Extracting Classes.."
        self.classes = Train.ExtractClasses(self.trainingSet)

    def train(self):
        print "Training NBC..."
        self.vocabulary, self.prior, self.condprob = Train.TrainMultinomialNaiveBayes(self.classes, self.trainingSet)

    def speed(self):
        testDocument = Data.GetDocument(self.testSet)
        print "The time is took to do a single application of the NBC on a document is", Test.TimeMeasure(self.classes, self.vocabulary, self.prior, self.condprob, testDocument), "seconds."
        
    def accuracyOnTrain(self):
        percentage = Test.Accuracy(self.classes ,self.vocabulary, self.prior, self.condprob, self.dataSet)
        print "The percentage of correct predictions is ",100*percentage,"percent."

    def accuracyOnTest(self):
        percentage = Test.Accuracy(self.classes, self.vocabulary, self.prior, self.condprob, self.testSet)
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
        self.labelFrame = LabelFrame(root,width=400,height=100, text="Enter Type:")
        self.labelFrame.grid_propagate(False)
        self.labelFrame.grid(row=1, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

        Checkbutton(self.labelFrame,text="E-mails",variable=self.CheckVar1,command=lambda:self.switchToType(0)).grid(row=0, column=0,sticky="W")
        Checkbutton(self.labelFrame,text="Blogs"  ,variable=self.CheckVar2,command=lambda:self.switchToType(1)).grid(row=1, column=0,sticky="W")
        Checkbutton(self.labelFrame,text="Jokes"  ,variable=self.CheckVar3,command=lambda:self.switchToType(2)).grid(row=2, column=0,sticky="W")

        self.labelFrame2 = LabelFrame(root,width=400,height=250, text="Operations:")
        self.labelFrame2.grid_propagate(False)
        self.labelFrame2.grid(row=4, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

        Button(self.labelFrame2, text="Gather Data", command=lambda:self.data()).grid(row=10, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)
        Button(self.labelFrame2, text="Train", command=lambda:self.train()).grid(row=11, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)
        Button(self.labelFrame2, text="Test the speed", command=lambda:self.speed()).grid(row=12, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)
        Button(self.labelFrame2, text="Test the accuracy on the testset", command=lambda:self.accuracyOnTrain).grid(row=13, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)
        Button(self.labelFrame2, text="Test the accuracy on the dataset", command=lambda:self.accuracyOnTest).grid(row=14, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

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
root.geometry(("420x390"))
app = Application(master=root)
app.mainloop()

    