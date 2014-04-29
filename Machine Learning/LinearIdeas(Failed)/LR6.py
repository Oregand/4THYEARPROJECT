from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np

# create data frame containing your data, each column can be accessed # by df['column   name']
df = pd.read_csv('output.csv')

target_names = np.array(['Positives','Negatives'])

# add columns to your data frame
targets = df['Targets']
df['is_train'] = np.random.uniform(0, 1, len(df)) <= 0.75
df['Type'] = pd.Categorical(targets, target_names)


# define training and test sets
train = df[df['is_train']==True]
test = df[df['is_train']==False]

trainTargets = np.array(train['Targets']).astype(int)
testTargets = np.array(test['Targets']).astype(int)

# columns you want to model
features = df.columns[0:7]

# call Gaussian Naive Bayesian class with default parameters
gnb = GaussianNB()

# train model
y_gnb = gnb.fit(train[features], trainTargets).predict(train[features])