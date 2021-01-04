#%%
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv', index_col=0, parse_dates=True)

# print(data['station_paris'])

data.plot.area(figsize=(15,4), subplots=True)

# %%
