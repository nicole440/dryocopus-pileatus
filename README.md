# dryocopus-pileatus
## eBird Data Retrieval

This project retrieves data from the eBird API using Python. It fetches species codes for all recorded observations in Pennsylvania (PA) and retrieves all recent observations in PA. The retrieved data is saved in CSV format for further analysis and processing. I haven't yet decided what I'd like to do with this information, but I'm just glad that I have it.

### Prerequisites

- Python 3.x
- Requests library
- pandas library
- dotenv library

### Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/nicole440/dryocopus-pileatus.git
   ```

2. Install the required dependencies using pip:

    ```bash
    pip install requests
    ```

3. Set up the API key:

    - Obtain an API key from the eBird website.
    - Create a .env file in the project root directory.
    - Add the following line to the .env file:

        ```
        EBIRD_API_KEY=your-api-key
        ```
        *Replace your-api-key with your actual eBird API key.*

### Usage
1. Run the main.py script:

    ```bash
    python main.py
    ```

    The script will make API calls to retrieve the species codes and recent observations data from eBird.

2. Data files:

    - The species codes for all recorded observations in PA will be saved as pa_species.csv.
    - The recent observations in PA will be saved as recent_observations.csv. You can use these CSV files for further analysis, processing, or visualization.


### Notes
The .env file is excluded from version control to protect your API key. Make sure not to commit it to your repository.
Remember to respect the terms of use and any applicable data usage guidelines provided by eBird when working with the data obtained from their API.