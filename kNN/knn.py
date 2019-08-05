import pandas as pd
import numpy as np
from scipy.spatial import distance
from sklearn.metrics.pairwise import manhattan_distances
df = pd.read_csv('dataset.csv',index_col=0)
df = df.replace('male',1)
df = df.replace('female',0)
method = input("Give distance formula : ")
a = input("Enter the Gender : ")
gender = 1 if a == 'male' else 0 
pointer,hsc = map(float, input("Give comma seprated attributes : ").split(","))
a = (gender,pointer,hsc)
dist = []
if method.lower() == 'euclidean':
    for i in range(0,len(df.index)):
        dist.append(distance.euclidean(a,df.iloc[i,:3]))
elif method.lower() == 'manhattan':
    temp = []
    for i in range(0,len(df.index)):
        temp.append(manhattan_distances([a],[df.iloc[i,:3]]))
    for i in range(0, len(df.index)):
        dist.append(temp[i][0][0])
else:
    print("Wrong input!")
df['distance'] = dist
df = df.sort_values(by=['distance'])
k = int(input("Value of K : "))
sort = df.iloc[:k,3].as_matrix()
p = f = 0
for i in range(0,k):
    if sort[i] == 'pass':
        p += 1
    else:
        f += 1
c = 'pass' if (p > f) else 'fail'
print("The result is : " + c)
print(df)