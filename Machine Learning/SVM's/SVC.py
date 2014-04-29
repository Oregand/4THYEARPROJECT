__author__ = 'davidoregan'

import numpy as np
import pandas as pd
from sklearn.feature_extraction import DictVectorizer

churn_df = pd.read_csv('wv_golfTraining.csv')





churn_result = churn_df['link']
churn_df.drop('link',axis=1,inplace=True)

churn_train = churn_df.tail(-500)
churn_train_result = churn_result.tail(-500)

churn_test = churn_df.head(500)
# Save test to a csv file
churn_test.to_csv("test_churn.csv")

dv = DictVectorizer()
dv.fit(churn_df.T.to_dict().values())


from sklearn.preprocessing import StandardScaler

yes_no_cols = ["price"]

scaler = StandardScaler()

# Feature matrix
X = dv.as_matrix().astype(np.float)
X = scaler.fit_transform(X)

# Target values
y = np.where(churn_result == 'True.',1,0)