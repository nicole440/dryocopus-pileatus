# Function for transformation of dataframes for hotspots by subregion
def transform_columns(dataframe):
    # Specify the columns to be dropped
    columns_to_drop = ['countryCode', 'subnational1Code']
    # Drop the specified columns from the DataFrame
    dataframe = dataframe.drop(columns=columns_to_drop)
    dataframe = dataframe.rename(columns={'locId': 'Location_ID', 'locName': 'Location_Name', 'subnational2Code': 'Sub-National_Code',
                                                 'lat': 'Latitude', 'lng': 'Longitude', 'latestObsDt': 'Date_of_Most_Recent_Observation', 
                                                 'numSpeciesAllTime': 'Total_Species_Recorded_at_Location'})
    return dataframe