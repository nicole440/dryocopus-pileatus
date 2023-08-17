# Function for transformation of dataframes for hotspots by subregion
def transform_columns(dataframe):
    # Specify the columns to be dropped
    columns_to_drop = ['countryCode', 'subnational1Code']
    # Drop the specified columns from the DataFrame
    dataframe = dataframe.drop(columns=columns_to_drop)
    dataframe = dataframe.rename(columns={'locId': 'location_id', 'locName': 'location_name', 'subnational2Code': 'sub_national_code',
                                                 'lat': 'latitude', 'lng': 'longitude', 'latestObsDt': 'date_recent_observation', 
                                                 'numSpeciesAllTime': 'total_species_recorded_at_location'})
    return dataframe