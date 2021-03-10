import pandas as pd

location_variants = {
    'Ottawa Division': 2251,
    'Ottawa Public Health': 2251,
    'OTTAWA INTL A': 2251,
    'Ottawa': 2251,
    'Toronto Division': 3895,
    'Toronto Public Health': 3895,
    'TORONTO CITY': 3895,
    'Toronto': 3895,
}

date_ids = {}


def load_dates():
    dates = pd.read_csv("dates.csv")
    print(dates.head())
    for index, row in dates.iterrows():
        d = int(row['day'])
        m = int(row['month'])
        y = int(row['year'])
        if d not in date_ids:
            date_ids[d] = {}
        if m not in date_ids[d]:
            date_ids[d][m] = {}
        date_ids[d][m][y] = row['id']


def get_date(query: str):
    split = query.split('-')
    y = int(split[0])
    m = int(split[1])
    d = int(split[2])
    print(f'{y}-{m}-{d}')
    return date_ids[d][m][y]


def handle_mobility():
    mobility = pd.read_csv("data_preprocessing/mobility_dimension.csv")
    locs = []
    dates = []
    print(mobility.head())
    for index, row in mobility.iterrows():
        locs.append(location_variants[row['metro_area']])
        dates.append(get_date(str(row['date'])))
    mobility.loc[:, 'location_id'] = locs
    mobility.loc[:, 'date_id'] = dates
    print(mobility.head())
    mobility.to_csv("data_preprocessing/mobility_dimension.csv", index=False)


def handle_weather():
    weather = pd.read_csv("data_preprocessing/weather_dimension.csv")
    locs = []
    dates = []
    print(weather.head())
    for index, row in weather.iterrows():
        locs.append(location_variants[row['city']])
        dates.append(get_date(str(row['Date/Time'])))
    weather['location_id'] = locs
    weather['date_id'] = dates
    print(weather.head())
    weather.to_csv("data_preprocessing/weather_dimension.csv", index=False)

def handle_special_measures():
    sm = pd.read_csv("special_measures.csv")
    s_dates = []
    e_dates = []
    print(sm.head())
    for index, row in sm.iterrows():
        s_dates.append(get_date(str(row['StartDate'])))
        e_dates.append(get_date(str(row['EndDate'])))
    sm['start_date_id'] = s_dates
    sm['end_date_id'] = e_dates
    print(sm.head())
    sm.to_csv("special_measures.csv", index=False)

def merge_special_measures_with_individual():
    sms = []
    sm = pd.read_csv("special_measures.csv")
    sm_ids = []
    for index, row in sm.iterrows():
        s_id = row['start_date_id']
        e_id = row['end_date_id']
        sms.append((row['StartDate'], row['EndDate'], row['ID'], row['includesOttawa'], row['includesToronto']))
    print(sms)

    ind_frame = pd.read_csv("individual_dimension.csv")
    for index, row in ind_frame.iterrows():
        sm_id = -1
        for special_measure in sms:
            if row['date'] >= special_measure[0] and row['date'] <= special_measure[1]:
                allow = (row['reporting_phu_city'] == 'Toronto' and special_measure[4] == 'yes') or (row['reporting_phu_city'] == 'Ottawa' and special_measure[3] == 'yes')
                if allow:
                    sm_id = int(special_measure[2])
                    if sm_id != 3: break
        sm_ids.append(sm_id)

    # print(sm_ids)
    ind_frame['special_measure_id'] = sm_ids
    ind_frame.to_csv("individual_dimension.csv", index=False)


load_dates()
print(date_ids)
# handle_mobility()
# handle_weather()
# handle_special_measures()
merge_special_measures_with_individual()
