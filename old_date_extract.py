import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, date, time, timedelta
import re
import pickle

df = pd.read_csv("korean_summit.csv")
df = df.drop_duplicates()
# print(df.head())


# Handle missing data
df['COMPOUND'] = df['COMPOUND'].fillna(0)

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

today_date = datetime.today()
# event_date = datetime(2018, 4, 13, 21, 0, 0)  # Date of Syria bombing announcement
# event_date = datetime(2018, 6, 12, 12, 0, 0)  # Date of Korean Summit
# # print(event_date)
temp_list = []
for index, row in df.iterrows():
    regex = re.findall(r"\d", row['DATE'])
    f_date = "".join(regex[0:14])
    datetime_object = datetime.strptime(f_date, '%Y%m%d%H%M%S')
    # print(datetime_object)
    t = today_date - datetime_object
    temp_list.append(t)

df['T_minus'] = temp_list

# Open pickled arrays and load
# file1 = open('syria_full_f1.pkl','r')
# file2 = open('syria_full_f2.pkl','r')
# f1 = pickle.load(file1)
# f2 = pickle.load(file2)

# Iterate through DataFrame and append to arrays
for index, row in df.iterrows():
	time = (row['T_minus'].days * 86400) + (row['T_minus'].seconds)
	# time = row['T_minus'].seconds 
	f1.append(time)
	print(time)
	f2.append(row['COMPOUND'])
	print(row['COMPOUND'])
    

# # Pickle arrays
# f1_file = open('korea_full_f1.pkl', 'wb')
# f2_file = open('korea_full_f2.pkl', 'wb')
# pickle.dump(f1, f1_file)
# pickle.dump(f2, f2_file)

# Plot data
plt.xlabel('Time (seconds)')
plt.ylabel('Compound sentiment score')
plt.scatter(f1, f2, c='black', s=1)
plt.show()
