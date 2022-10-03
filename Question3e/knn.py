#-------------------------------------------------------------------------
# AUTHOR: Rida Siddiqui
# FILENAME: knn.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #2 - Question 3
# TIME SPENT: 2 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn.neighbors import KNeighborsClassifier
import csv

db = []

#reading the data in a csv file
with open('binary_points.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)


label = {
        "+": 2.0,
        "-": 1.0
    }
predictions = []
#loop your data to allow each instance to be your test set
for i, instance in enumerate(db):
    # add the training features to the 2D array X and remove the instance that will be used for testing in this iteration.
    # For instance, X = [[1, 3], [2, 1,], ...]]. Convert values to float to avoid warning messages
    testSample = db[i]
    #print("testSample", testSample)

    X = []
    Y = []
    training_data = []
    for row in db:
        if row != testSample:
            #print("row", row)
            column1 = float(row[0])
            column2 = float(row[1])

            training_data = [column1, column2]
            #print("training_data", training_data)

            X.append(training_data)
            Y.append(label[row[2]])
    #testSample
    x = float(testSample[0])
    y = float(testSample[1])
    testSample = [x, y]

    print()
    print("Test Sample: ", testSample)
    print ("X: ", X)
    print ("Y: ", Y)


    #transform the original training classes to numbers and add them to the vector Y. Do not forget to remove the instance that will be used for testing in this iteration.
    #For instance, Y = [1, 2, ,...]. Convert values to float to avoid warning messages

    #--> add your Python code here
    # X =
    # Y =
    #testSample =

    #fitting the knn to the data
    clf = KNeighborsClassifier(n_neighbors=1, p=2)
    clf = clf.fit(X, Y)

    #use your test sample in this iteration to make the class prediction. For instance:
    #class_predicted = clf.predict([[1, 2]])[0]
    #--> add your Python code here
    class_predicted = clf.predict([testSample])[0]
    #print("class_predicted", class_predicted)



    #compare the prediction with the true label of the test instance to start calculating the error rate.
    #--> add your Python code here
    #class_predicted

    true_label = label[db[i][2]]

    if true_label == class_predicted:
        predictions.append(1)
        #corect predictions
    else:
        predictions.append(0)
        #wrong prediction

#print the error rate
error_rate = predictions.count(0)/len(predictions)
print("Error Rate: ", error_rate)






