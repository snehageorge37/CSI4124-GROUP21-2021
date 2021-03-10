import pandas as pd
import numpy as np

to_remove = ['source']
r_data = pd.read_csv(filepath_or_buffer="special_measures_original.csv")

r_data = r_data.drop(columns=to_remove)
print(r_data.shape)
r_data = r_data.sort_values('StartDate')
r_data.to_csv("special_measures.csv", index=False)