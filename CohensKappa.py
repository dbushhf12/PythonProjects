import pandas as pd
import sklearn 
import sklearn.metrics
import statistics 
import itertools
import math

#import csv with raw data
data = pd.read_csv('[FileLocation]')

result = {}  #dictionary to store kappa scores
sum = 0 #variable to store cumsum of kappa scores
counter = 0 #counter that will increase to the total number of scores (adds 1 each increment of the for loop) 
for c in data.columns: #populates dictionary with values from imported csv
    result[c]={}

for x in itertools.combinations(data.columns,2): #creates labels for all unique pairs in dictionary 
    result[x[0]][x[1]]=sklearn.metrics.cohen_kappa_score(data[x[0]],data[x[1]]) #assigns each label (unique pair) a kappa score
    sum = sum + result[x[0]][x[1]] #calculates cumsum of kappa scores
    counter+=1 #increases counter by 1 each iteration
avg = sum/counter #calculates average kappa score by dividing cumsum of kappa scores by total number of scores

#determine strength of average kappa score
if (avg <= 0.2):
    strength = 'NONE'
elif (avg >0.2 and  avg <= 0.39):
    strength = 'MINIMAL'
elif (avg >0.39 and avg <=0.59):
    strength = 'WEAK'
elif (avg >0.59 and avg <=0.79):
    strength = 'MODERATE'
elif (avg >0.70 and avg <=0.90):
    strength = 'STRONG'
elif (avg >0.90 and avg <1.00):
    strength = 'VERY STRONG'
else:
    strength = 'THIS IS PROBABLY FAKE DATA'

df = pd.DataFrame(result) #convert dictionary to data frame 
df.loc[df.index[0], 'Total Avg'] = avg #add new data frame column for average kappa score
df.loc[df.index[0], 'Strength'] = strength #add new data frame column for strength of average kappa score

df.to_csv('[FileLocation]')
