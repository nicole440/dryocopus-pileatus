# Function for transformation of dataframes for hotspots by subregion
import requests
import pandas as pd
import time

import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get('EBIRD_API_KEY')

def fetch_hotspot_data(hotspots):
    hotspot_data_list = []
    
    for hotspot in hotspots:
        hotspots_url = 'https://api.ebird.org/v2/ref/hotspot/' + hotspot + '?fmt=json'
        try:
            response = requests.get(hotspots_url, params=api_key)
            response.raise_for_status()  # Raise an exception for bad status codes

            hotspots_data = response.json()
            hotspots_df = pd.DataFrame(hotspots_data)
            hotspot_data_list.append(hotspots_df)

            time.sleep(1)  # Add a 1-second delay to avoid rate limits
        except requests.exceptions.RequestException as e:
            print(f"An error occurred for hotspot {hotspot}: {e}")
            print(response.content)

    # Concatenate all DataFrames in the list into a single DataFrame
    all_hotspots_df = pd.concat(hotspot_data_list, ignore_index=True)

    return all_hotspots_df