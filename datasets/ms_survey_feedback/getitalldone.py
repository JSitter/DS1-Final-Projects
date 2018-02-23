#!/usr/bin/env python

import glob
import pandas as pd
from collections import Counter

df = pd.DataFrame(columns=["Week", "City","Timestamp", "Overall Satisfaction", "Pacing"])



# letus = glob.glob('datasets/ms_survey_feedback/2016/Anon Week 1 Feedback - LA.csv')
# print(letus)

#Get all files except for wierdy week 8 one
filenames = glob.glob('./2016/Anon Week * Feedback - *.csv')
cols = list()
all_headers = list()


for file_name in filenames:
    
    file_data = file_name.split(" ")
    week = file_data[2]

    city = file_data[-1].split('.')

    # print("city", city[0])
    # print("week", week)

    file_df = pd.read_csv(file_name)
    
    cols.append(len(list(file_df)))
    all_headers.extend(list(file_df))

num_headers = Counter(all_headers)
#print(all_headers)
print("number of headers", num_headers)
print(set(cols))
