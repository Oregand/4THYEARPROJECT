__author__ = 'davidoregan'

from sklearn.naive_bayes import MultinomialNB
import codecs
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import metrics
from operator import itemgetter
from sklearn.metrics import classification_report
import csv
import numpy as np
from sklearn.svm import LinearSVC
import os

#os.chdir('/Users/rweiss/Dropbox/presentations/MozFest2013/data/')

#note that if you generated this from R, you will need to delete the row
#"NYT_sample.Topic.Code","NYT_sample.Title"
#from the top of the file.

#Look at this Nigga thinking hes cool and shit, but guess what?
# Ima classifiy the fuck out of my car's file by price,
# given the same model of car we will train via price like a bause

nyt = open('../SVM')  # check the structure of this file!
nyt_data = []
nyt_labels = []
csv_reader = csv.reader(nyt)
title = []

for line in csv_reader:
    nyt_labels.append((line[2]))
    nyt_data.append(line[2])

for titles in csv_reader:
    title.append((titles[0]))


nyt.close()



trainset_size = int(round(len(nyt_data) * 0.75))  # i chose this threshold arbitrarily...to discuss
print 'The training set size for this classifier is ' + str(trainset_size) + '\n'

X_train = np.array([''.join(el) for el in nyt_data[0:trainset_size]])
y_train = np.array([el for el in nyt_labels[0:trainset_size]])

X_test = np.array([''.join(el) for el in nyt_data[trainset_size + 1:len(nyt_data)]])
y_test = np.array([el for el in nyt_labels[trainset_size + 1:len(nyt_labels)]])

#print(X_train)

vectorizer = TfidfVectorizer(min_df=2,
                             ngram_range=(1, 2),
                             stop_words='english',
                             strip_accents='unicode',
                             norm='l2')

test_string = unicode(nyt_data[0])

print "Example string: " + test_string
print "Preprocessed string: " + vectorizer.build_preprocessor()(test_string)
print "Tokenized string:" + str(vectorizer.build_tokenizer()(test_string))
print "N-gram data string:" + str(vectorizer.build_analyzer()(test_string))


X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)






svm_classifier = LinearSVC().fit(X_train, y_train)



y_svm_predicted = svm_classifier.predict(X_test)
print "MODEL: Linear SVC\n"

print 'The precision for this classifier is ' + str(metrics.precision_score(y_test, y_svm_predicted))
print 'The recall for this classifier is ' + str(metrics.recall_score(y_test, y_svm_predicted))
print 'The f1 for this classifier is ' + str(metrics.f1_score(y_test, y_svm_predicted))
print 'The accuracy for this classifier is ' + str(metrics.accuracy_score(y_test, y_svm_predicted))


print '\nHere is the classification report:'
brolo = classification_report(y_test, y_svm_predicted)
print brolo

#simple thing to do would be to up the n-grams to bigrams; try varying ngram_range from (1, 1) to (1, 2)
#we could also modify the vectorizer to stem or lemmatize
print '\nHere is the confusion matrix:'
yolo = metrics.confusion_matrix(y_test, y_svm_predicted, labels=(nyt_labels))
print yolo

#Save output to file
output = open('../SVM', 'w')
for x, value in np.ndenumerate(brolo):
	output.write(str((value)))
	output.write("\n")
output.close()




