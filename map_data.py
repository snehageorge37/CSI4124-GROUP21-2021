import pandas as pd

location_variants = {
    'Ottawa Division': 2251,
    'Ottawa Public Health': 2251,
    'OTTAWA INTL A': 2251,
    'Toronto Division': 3895,
    'Toronto Public Health': 3895,
    'TORONTO CITY': 3895
}


def handle_mobility():
    mobility = pd.read_csv("data_preprocessing/mobility_dimension.csv")
    locs = []
    print(mobility.head())
    for index, row in mobility.iterrows():
        locs.append(location_variants[row['metro_area']])
    mobility.loc[:, 'location_id'] = locs
    print(mobility.head())
    mobility.to_csv("data_preprocessing/mobility_dimension.csv", index=True)


def handle_weather():
    weather = pd.read_csv("data_preprocessing/weather_dimension.csv")
    locs = []
    print(weather.head())
    for index, row in weather.iterrows():
        locs.append(location_variants[row['city']])
    weather.loc[:, 'location_id'] = locs
    print(weather.head())
    weather.to_csv("data_preprocessing/weather_dimension.csv", index=True)


handle_weather()
