import pandas as pd

location_variants = {
    'Ottawa Division': 2251,
    'Ottawa Public Health': 2251,
    'OTTAWA INTL A': 2251,
    'Toronto Division': 3895,
    'Toronto Public Health': 3895,
    'TORONTO CITY': 3895
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
    mobility.to_csv("data_preprocessing/mobility_dimension.csv", index=True)


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
    weather.to_csv("data_preprocessing/weather_dimension.csv", index=True)


load_dates()
print(date_ids)
handle_mobility()
handle_weather()
