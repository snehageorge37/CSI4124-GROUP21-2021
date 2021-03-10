import pandas as pd
import numpy as np

# import datetime as dt

# start_date = dt.datetime(year=2020, month=4, day=1)
# end_date = dt.datetime(year=2020, month=7, day=31)

to_remove = ['PHU_url']
r_data = pd.read_csv(filepath_or_buffer="restriction.csv")
# print(phu_data.columns)
# print(phu_data)
r_data = r_data.drop(columns=to_remove)
print(r_data.shape)

# Filter out region
index_names = r_data[np.logical_and(r_data['Reporting_PHU_id'] != 3895, r_data['Reporting_PHU_id'] != 2251)].index
r_data.drop(index_names, inplace=True)
print(r_data.shape)

r_data = r_data.sort_values('start_date')
r_data.to_csv("restriction_dimension.csv", index=False)

# There are many units under Toronto Public Health, how do we handle that?
