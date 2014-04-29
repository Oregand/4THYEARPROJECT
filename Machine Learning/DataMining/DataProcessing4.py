__author__ = 'davidoregan'


import json

import numpy as np
import copy
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pylab as plt2
from scipy.stats import pearsonr
from datetime import datetime
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics.pairwise import cosine_similarity



from sklearn import svm, tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.linear_model import RidgeClassifier
from sklearn.svm import LinearSVC
from sklearn.linear_model import SGDClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestCentroid
from sklearn.utils.extmath import density
from sklearn import metrics



''' All Dem imports  '''


big_table = pd.read_csv('output.csv', encoding='utf-8')
big_table = big_table[big_table['title'] != "deleted"]



def get_author_stats():
    author_table = big_table.groupby('title')
    author_count = author_table['title'].count()
    author_count.sort()
    return author_count

author_count = get_author_stats()
author_count[-10:]


print "Number of posts: ", len(big_table)
print "Number of distinct authors: ", len(big_table .groupby('title'))
print get_author_stats()

#plt.hist(author_count, bins = 20, log=True)
#plt.title("Distribution of number of submissions")
#remove_border()


types = list(big_table['title'].unique())

'''
returns:
- the number of active users with more than 2 posts
- the number of distinct authors
- the ratio of active/distinct users
for a subreddit
'''
def get_sub_stats(subreddit):
    author_table = subreddit.groupby('title')
    dist_authors = len(subreddit.groupby('title'))
    #print "Number of distinct authors: ", dist_authors
    successful_authors = subreddit[author_table.transform(lambda x: x.count() > 1).astype('bool')]
    authorset = set()
    for a in successful_authors.index:
        authorset.add(successful_authors.ix[a]['title'])
    active_users = len(authorset)
    #print "number of authors with more than 1 submission in the top 1000: ", active_users
    if dist_authors >0:
        succ_ratio = float(active_users) / dist_authors
    else:
        succ_ratio = 0
    return active_users, dist_authors, succ_ratio

#get the values for all types of data
authorstats = {}
for ctype in types:
    curr_df = big_table[big_table['title'] == ctype]
    authorstats[ctype] = get_sub_stats(curr_df)
del curr_df #reduce memory

'''
plots a scatterplot for a list of subreddit stats calculated before
X-Axis: Number of distinct users
Y-Axis: Success ratio
'''

def plot_author_success(successlist):
    xvals = [value[0] for key, value in successlist.iteritems()]
    yvals = [value[2] for key, value in successlist.iteritems()]
    labellist = [key for key, value in successlist.iteritems()]

    fig, ax = plt.subplots()
    ax.scatter(xvals, yvals)

    for i, txt in enumerate(labellist):
        ax.annotate(txt, (xvals[i],yvals[i]))
    plt.title("Active Users with their success rate")
    plt.xlabel("No. distinct users")
    plt.ylabel("fraction of users with multiple posts")
    #remove_border()

plot_author_success(authorstats)



#regression line
m_fit,b_fit = plt2.polyfit(big_table.comments, big_table.score, 1)
plt2.plot(big_table.comments, big_table.score, 'yo', big_table.comments, m_fit*big_table.comments+b_fit, color='purple', alpha=0.3)
plt.title("Comments versus Score")
plt.xlabel("price")
plt.ylabel("title")
plt.xlim(-10, max(big_table.comments) * 1.05)
plt.ylim(-10, max(big_table.score) * 1.05 )

