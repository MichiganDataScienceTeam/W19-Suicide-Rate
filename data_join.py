import pandas as pd
import numpy as np

master_df = pd.read_csv('master.csv')
who_df = pd.read_csv('who_suicide_statistics.csv')
who_df_new = who_df.loc[who_df['year'].isin([1985, 1986, 2015, 2016])]
data_df = pd.concat([master_df, who_df_new], sort=True)
data_df.sort_values('year')

data_df.to_csv('joinedkaggledata.csv', index=False)