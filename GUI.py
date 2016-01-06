from data import Data
from train import Train
from classify import Classify
from test import Test
from Tkinter import *
from tkFileDialog import *
import pickle

class Application(Frame):

    def data(self):
        datasets = [{"trainSet": "mails-train", "testSet": "mails-test"}, {"trainSet": "blogs-train", "testSet": "blogs-test"}]
        if self.CheckVar1.get() == 1:
            dataset = datasets[0]
        if self.CheckVar2.get() == 1:
            dataset = datasets[1]
        print "Creating Train File..."
        Data.CreateDataFile(dataset['trainSet'], dataset['trainSet'] + ".txt")
        print "Initializing Train File..."
        self.trainingSet = Data.LoadFile(dataset['trainSet'] + ".txt")
        print "Creating Test File..."
        Data.CreateDataFile(dataset['testSet'], dataset['testSet'] + ".txt")
        print "Initializing Test File..."
        self.testSet = Data.LoadFile(dataset['testSet'] + ".txt")
        print "Extracting Classes.."
        self.classes = Train.ExtractClasses(self.trainingSet)
        print "Done."

    def train(self):
        self.data()
        print "Training NBC..."
        self.vocabulary, self.prior, self.condprob = Train.TrainMultinomialNaiveBayes(self.classes, self.trainingSet)
        print "Done."
        self.save()

    def speed(self):
        testDocument = Data.GetDocument(self.testSet)
        print "The time is took to do a single application of the NBC on a document is", Test.TimeMeasure(self.classes, self.vocabulary, self.prior, self.condprob, testDocument['document']), "seconds."
        print "Done."
        
    def accuracyOnTrain(self):
        print "Calculating Accuracy..."
        percentage = Test.Accuracy(self.classes ,self.vocabulary, self.prior, self.condprob, self.trainingSet)
        print "The percentage of correct predictions is ",100*percentage,"percent."
        print "Done."

    def accuracyOnTest(self):
        print "Calculating Accuracy..."
        percentage = Test.Accuracy(self.classes, self.vocabulary, self.prior, self.condprob, self.testSet)
        print "The percentage of correct predictions is ",100*percentage,"percent."
        print "Done."
        
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

    def save(self):
        f = asksaveasfile(mode='w', defaultextension=".train")
        if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
            return
        file2save = [self.classes, self.vocabulary, self.prior, self.condprob]
        pickle.dump(file2save, f) 
        f.close() # `()` was missing.
        print "Saved."

    def load(self):
        f = askopenfile(mode='r', defaultextension=".train")        
        if f is None: # askopenfile return `None` if dialog closed with "cancel".
            return
        self.classes, self.vocabulary, self.prior, self.condprob =  pickle.load(f)

        datasets = [{"trainSet": "mails-train", "testSet": "mails-test"}, {"trainSet": "blogs-train", "testSet": "blogs-test"}]
        if self.CheckVar1.get() == 1:
            dataset = datasets[0]
        if self.CheckVar2.get() == 1:
            dataset = datasets[1]
        self.testSet = Data.LoadFile(dataset['testSet'] + ".txt")
        f.close() # `()` was missing.
        print "Loaded."

    def testSingleFile(self):
        f = askopenfile(mode='r', defaultextension=".txt")
        if f is None: # askopenfile return `None` if dialog closed with "cancel".
            return
        lines = f.read()
        bagOfWords = re.split(' ',lines)
        singleFile = Data.Normalize(bagOfWords)

        print "Loaded."
        print "Calculating..."
        topClass, score = Classify.ApplyMultinomialNaiveBayes(self.classes, self.vocabulary, self.prior, self.condprob, singleFile)
        print "This document belongs to", topClass
        print "Done."
        f.close() # `()` was missing.
       

    def createWidgets(self):
        self.labelFrame = LabelFrame(root,width=400,height=100, text="Enter Type:")
        self.labelFrame.grid_propagate(False)
        self.labelFrame.grid(row=1, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

        Checkbutton(self.labelFrame,text="E-mails",variable=self.CheckVar1,command=lambda:self.switchToType(0)).grid(row=0, column=0,sticky="W")
        Checkbutton(self.labelFrame,text="Blogs"  ,variable=self.CheckVar2,command=lambda:self.switchToType(1)).grid(row=1, column=0,sticky="W")

        self.labelFrame2 = LabelFrame(root,width=400,height=250, text="Operations:")
        self.labelFrame2.grid_propagate(False)
        self.labelFrame2.grid(row=4, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)
        Button(self.labelFrame2, text="Train Classifier", command=lambda:self.train()).grid(row=11, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)
        Button(self.labelFrame2, text="Load Pretrained Classifier", command=lambda:self.load()).grid(row=12, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)
        Button(self.labelFrame2, text="Test the speed", command=lambda:self.speed()).grid(row=13, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)
        Button(self.labelFrame2, text="Test the accuracy on the test set", command=lambda:self.accuracyOnTest()).grid(row=14, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

        self.labelFrame3 = LabelFrame(root,width=400,height=80, text="Test on single file:")
        self.labelFrame3.grid_propagate(False)
        self.labelFrame3.grid(row=7, column=0, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)

        Button(self.labelFrame3, text="Load", command=lambda:self.testSingleFile()).grid(row=11, column=2, sticky='W', padx=5, pady=5, ipadx=5, ipady=5)




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
root.geometry(("420x530"))
app = Application(master=root)
app.mainloop()

    