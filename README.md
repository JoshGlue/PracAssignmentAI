REQUIREMENTS
Windows, linux, OS X
python 2.7 (https://www.python.org/download/releases/2.7/)

INSTALLATION
The installation is straightforward and simple: you just need to unzip the src code to a directory. 

RUNNING THE APPLICATION
When the files are unzipped, you need to open the terminal or command line that is provided by your system. 
Then type the command: cd {location where the src code is}
Followed by: python GUI.py
If everything is installed correctly, then a GUI will start up.

APPLICATION MANUAL

The basics
Our Interactive learner is based on documents that are provided by Blackboard. These document consists of emails and blogs. These documents are stored in folders in the form of text files. Where the text file is stored determines if it is a blog or an email. The folders are subdivided by subfolders, these sub folders correspond to the possible classes. So the file structure can look like this:
-Email
------Spam
----------Spam01.txt
------Msg
----------msg01.txt

-Blog
-----M
------Blog_written_by_male_01.txt
-----F
------Blog_written_by_female_01.txt

So the directory structure corresponds to what kind of document it is and to what class it belongs to. To add new documents to the classes, you just need to copy and paste a document in the correct directory.

Train data and test data
The train data that we provide are in blogs-train, respectively mails-train and the test data is located in blogs-test and mails-test.


GUI
Our GUI is a user friendly interface to execute basic functions of our application. 
It consists of one window and the output of the actions will be shown in the terminal or command line. The actions that can be done are selecting different types of documents, train the classifier, load a pretrained classifier, test the speed of the Interactive Learner and Apply the classifier on a single document. The documents that can be selected are of the kind of mails and blogs (provided by the AI blackboard Page).

Select Type
These checkboxes need to be checked if the correct type of document is checked.

Train Classifier
This button will train the classifier based on the documents that are provided in the train directory. When a document is added, changed or removed, the training needs to be run again. After the training of the classifier has finished, a dialog will pop up where you can store the classifier if you want to.

Load Pretrained Classifier
Here you can load a already trained classifier to save effort of training the data again when a new session has been started. We provide a pretrained blogs classifier and mails classifier called blogs.train and mails.train

Test the speed
The speed of the classification of a random single document is provided.

Test the accuracy on the test set
The classifier classifies all the documents that are present in the test folder and then gives a score back of the accuracy of the classifier based on the test documents. 

Test on single document
Here you can classify a document that is provided by the user itself.