import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt

df = pd.read_csv("bitcoin_auto.csv")
df = df.drop_duplicates()
# print(df.head())


# Handle missing data
df['COMPOUND'] = df['COMPOUND'].fillna(0)
df['NEGATIVE'] = df['NEGATIVE'].fillna(0)
df['NEUTRAL'] = df['NEUTRAL'].fillna(0)
df['POSITIVE'] = df['POSITIVE'].fillna(0)


# Convert to boolean values
# df['NEGATIVE'] = df['NEGATIVE'].round(0).astype(np.int).abs()
# df['NEUTRAL'] = df['NEUTRAL'].round(0).astype(np.int).abs()
# df['POSITIVE'] = df['POSITIVE'].round(0).astype(np.int).abs()
# df.info()

# Convert to percentages
# for index, row in df.iterrows():
#     temp = row['COMPOUND']
#     temp = float(temp) * 100
#     row['COMPOUND'] = temp

# df['COMPOUND'] = df['COMPOUND'].astype(np.int)

# for index, row in df.iterrows():
#     temp = row['POSITIVE']
#     temp = float(temp) * 100
#     row['POSITIVE'] = temp

# df['POSITIVE'] = df['POSITIVE'].astype(np.int)

hard_date = dt.date(2013, 5, 2)
temp_list = []
for index, row in df.iterrows():
	t = hard_date
	temp_list.append(t)

df['T_minus'] = temp_list
df.info()
# df['POSITIVE'] = df['POSITIVE'].astype(np.int)
# # df.info()
# print(df['POSITIVE'])
# outfile = open("values.txt", "w")
# for value in df['NEGATIVE'].values:
#     outfile.write(value)

# f1 = df['COMPOUND'].values
# f2 = df['POSITIVE'].values
# # f3 = df['POSITIVE'].values
# #
# X = np.matrix(zip(f1, f2))
# kmeans = KMeans(n_clusters=2).fit(X)
# # wh1.insert((wh1.shape[1]),'kmeans',kmeans)

# # Plot Data
# fig = plt.figure()
# ax = fig.add_subplot(111)
# scatter = ax.scatter(kmeans,kmeans,
#                      c=kmeans[0],s=50)
# ax.set_title('K-Means Clustering')
# ax.set_xlabel('COMPOUND')
# ax.set_ylabel('POSITIVE')
# plt.colorbar(scatter)

