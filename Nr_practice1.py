# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 13:05:58 2019

@author: Hari
"""

#import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
#import os
#import random
#import math
#from sklearn.cluster import KMeans
#
#dataset=pd.read_csv('C:/Users/Hari/Desktop/datasets/Naresh_datasets/Datasets/Universities.csv')
#
#x = dataset.iloc[:,[1,5]].values
#x
#
#km = KMeans(n_clusters=4,init='k-means++',max_iter=300,n_init=10,random_state=0)
#y_km = km.fit_predict(x)
#km.cluster_centers_
#
##visualizing clusters
#
#plt.scatter(x[y_km==0,0],x[y_km==0,1],c='red',label='Cluster 1')
#plt.scatter(x[y_km==1,0],x[y_km==1,1],c='blue',label='Cluster 2')
#plt.scatter(x[y_km==2,0],x[y_km==2,1],c='green',label='Cluster 3')
#plt.scatter(x[y_km==3,0],x[y_km==3,1],c='cyan',label='Cluster 4')
#plt.scatter(x[y_km==0,0],x[y_km==0,1],c='red',label='Cluster 1')
##plt.scatter(x[y_km==0,0],x[y_km==0,1],c='red',label='Cluster 1')
#plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],s=300,c='yellow',label='Centroids')
#plt.title('cluster of univeristy')
#
##plt.scatter(x,y_km)
#plt.legend()
#plt.show()
#
##concatinating the labels and data sets
#
#s1_grps = pd.Series(km.labels_) # centers
#s2_univs = dataset.iloc[:,0] 
#rslt = pd.concat([s1_grps,s2_univs],axis=1)#DataFrame(dict(s1 = s1_grps, s2 = s2_univs))
#rslt
#
#km.cluster_centers_
#df = pd.DataFrame(km.cluster_centers_)
#df.columns = ('Sat Score','Expenses')
#df
#
#s1_grps = pd.Series(km.labels_)
#s2_univs = dataset.iloc[:,:]
#rslt = pd.concat([s1_grps,s2_univs],axis=1)
#
#rslt
#
##***
#
## working with n-dimenstional cluster
#
#X = dataset.iloc[:,[1,2,3,4,5,6]].values
#X
#from sklearn.cluster import KMeans
#km=KMeans(n_clusters=5,init='k-means++',max_iter=300,n_init=10,random_state=0)
#y_km=km.fit_predict(X)
#y_km
#
#
#
##Visualizing the clusters
#plt.scatter(X[y_km==0,0],X[y_km==0,1],c='red',label='Cluster 1')
#plt.scatter(X[y_km==1,0],X[y_km==1,1],c='blue',label='Cluster 2')
#plt.scatter(X[y_km==2,0],X[y_km==2,1],c='green',label='Cluster 3')
#plt.scatter(X[y_km==3,0],X[y_km==3,1],c='cyan',label='Cluster 4')
#plt.scatter(X[y_km==4,0],X[y_km==4,1],c='pink',label='Cluster 5')
#plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],s=300,c='yellow',label='Centroids')
#plt.title('Clusters of Universities')
#plt.legend()
#plt.show()
#
##centers = pd.DataFrame(km.cluster_centers_)
##
##centers["clusters"] = range(5) #n_clusters
##dataset["ind"] = dataset.index
##dataset = dataset.merge(centers)
##dataset.sample(5)
##
##dataset = dataset.sort_values("ind")
##dataset = dataset.drop("ind",1)
#

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import random
import math
from sklearn.cluster import KMeans

data = pd.read_csv('C:/Users/Hari/Desktop/datasets/Naresh_datasets/Datasets/Mall_Customers.csv')

X = data.iloc[:,[3,4]].values
kmeans = KMeans(n_clusters=5,init='k-means++',random_state=42,max_iter=300)

y_kmeans = kmeans.fit_predict(X)

# Visualising the clusters
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s = 100, c = 'cyan', label = 'Cluster 4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s = 100, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 300, c = 'yellow', label =
'Centroids')
plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.show()
#plt.legend()


#plotting elow curve
wss = []
for i in range(1,5):
    kmeans = KMeans(n_clusters=i,random_state=0)
    kmeans.fit(X)
    wss.append(kmeans.inertia_)
    
plt.plot(range(1,5),wss)
plt.ylabel('wss')
plt.xlabel('number of clusters')




















