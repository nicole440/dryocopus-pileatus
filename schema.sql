DROP TABLE IF EXISTS Recent_Observations;

CREATE TABLE Recent_Observations (
	Index SERIAL PRIMARY KEY,
	Species_Code VARCHAR,
    Common_Name VARCHAR,
    Scientific_Name VARCHAR,
    Location_ID VARCHAR,
    Location_Name VARCHAR,
    Observation_Date DATE,
    Quantity_Observed INTEGER,
    Latitude VARCHAR,
    Longitude VARCHAR,
    Location_Private BOOLEAN
);
