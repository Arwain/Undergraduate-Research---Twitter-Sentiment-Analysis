
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, date, time, timedelta
import re
import pickle
import time as tm


df = pd.read_csv("bitcoin_auto.csv", dtype={"COMPOUND": float})
df = df.drop_duplicates()
# print(df.head())
df.info()
# tm.sleep(120)

# Handle missing data
# df['COMPOUND'] = df['COMPOUND'].fillna(0)


# today_date = datetime.today()
# event_date = datetime(2018, 4, 13, 21, 0, 0)  # Date of Syria bombing announcement
# event_date = datetime(2018, 6, 12, 12, 0, 0)  # Date of Korean Summit
# print(event_date)


temp_list = []
for index, row in df.iterrows():
    f_date = row['DATE'][4:20]
    year = row['DATE'][26:]
    f_date = f_date + year
    # print(f_date)
    regex = re.findall(r"[a-zA-Z]|\d", f_date)
    f_date = "".join(regex)
    datetime_object = datetime.strptime(f_date, '%b%d%H%M%S%Y')
    # print(datetime_object)
    t = today_date - datetime_object
    # print(t)
    temp_list.append(t)

df['T_minus'] = temp_list
f1 = []
f2 = []
for index, row in df.iterrows():
	time = (row['T_minus'].days * 24) + (row['T_minus'].seconds/3600)
	# time = row['T_minus'].seconds 
	f1.append(time)
	print(time)
	f2.append(row['COMPOUND'])
	# print(row['COMPOUND'])

# print(len(f1))
# print(len(f2))

# Pickle arrays
f1_file = open('btc_hours_f1.pkl', 'wb')
f2_file = open('btc_hours_f2.pkl', 'wb')
pickle.dump(f1, f1_file)
pickle.dump(f2, f2_file)

# Plot Data
plt.xlabel('Time(hours)')
plt.ylabel('Compound sentiment score')
plt.scatter(f1, f2, c='black', s=1)
plt.show()
