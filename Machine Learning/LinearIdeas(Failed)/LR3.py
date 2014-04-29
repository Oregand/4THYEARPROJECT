import pandas as pd
import csv

#Load csv into pandas dataframe
df = pd.read_csv('carData.csv')

#Load csv into pandas dataframe and set an index column
df =pd.read_csv('carData.csv', index_col = 'title')

#Load csv into pandas dataframe w/out Excel dialect
dia = csv.excel()
dia.quaoting = csv.QUOTE_NONE
df = pd.read_csv('carData.csv', index_col='title', dialect=dia)


