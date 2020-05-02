#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# %%
data=pd.read_excel('MCM_NFLIS_Data.xlsx','Data')
data

# %%
data['rate']=data.TotalDrugReportsCounty/data.TotalDrugReportsState
data.head()

# %%
data.pivot_table(['rate'], aggfunc=[sum], columns=['YYYY'], index=['FIPS_State'])

# %%
data.describe()

# %%
data.isnull()

# %%
