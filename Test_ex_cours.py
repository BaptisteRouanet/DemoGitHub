import numpy as np

arr_a = np.arange(10)
arr_b = arr_a[::-1]
np.all(arr_a >= 2)
np.any(arr_a < 1)

print(arr_a, arr_b, np.where(arr_a < 1), np.all(arr_a >= 2))
print(arr_a[arr_b > 5])

import pandas as pd

df = pd.DataFrame([[84,90,0,0],[0,0,46,78],[0,123,0,0]])
df.index = ['Air Canada','Jazz', 'WestJet']
df.columns = ['Airbus','Boeing','Bombardier','De Havilland']
df.sum() # Somme par compagnie a´erienne (lignes)
df['Total'] = df.sum(axis=1) # Somme par categorie d'avion (colonnes)
df['Double'] = df['Total']*2 # Creation de colonnes (`a la fin)
df.insert(6,'Triple',df['Total']*3) # Creation de colonnes

print(df)

import matplotlib.pyplot as plt
fig,axs = plt.subplots(nrows=2,ncols=3,sharex=True,
sharey=False,figsize=(12,7))
axs[1,2].plot(x,y)
axs[1,2].set_xlabel('x')

