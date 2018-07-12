
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, date, time, timedelta
import re
import pickle
import time as tm
from matplotlib import style
style.use("ggplot")

# Open pickled arrays and load
file1 = open('korea_f1.pkl','r')
file2 = open('korea_f2.pkl','r')
f1 = pickle.load(file1)
f2 = pickle.load(file2)

# Build model
X = np.array(list(zip(f1, f2)))
# Number of clusters
# k = 4
# # X coordinates of random centroids
# C_x = np.random.randint(0, np.max(X)-20, size=k)
# # Y coordinates of random centroids
# C_y = np.random.randint(-1, 1, size=k)
# C = np.array(list(zip(C_x, C_y)), dtype=np.float64)
# print(C)

# plt.scatter(f1, f2, c='#050505', s=7)
# plt.scatter(C_x, C_y, marker='*', s=200, c='b')
# Number of clusters
kmeans = KMeans(n_clusters=100)
# Fitting the input data
kmeans.fit(X)
# Getting the cluster labels
labels = kmeans.labels_
# Centroid values
centroids = kmeans.cluster_centers_
print(X)
# print(centroids)
# print(labels)


# Code below will plot color coded data
# Warning: Will increase time!
# color = ["g.","r.","b.","c.","m.","y.", "k.", "w."]
# for i in range(len(X)):
    # print("coordinate:", X[i][0], X[i][1], "label:", labels[i])
    # plt.plot(X[i][0], X[i][1], color[labels[i]], markersize = 1)

# Plot Data
plt.xlabel('Hours leading up to summit')
plt.ylabel('Compound sentiment score')
plt.scatter(f1, f2, c='black', s=1)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', s=100, c='blue')
plt.show()
