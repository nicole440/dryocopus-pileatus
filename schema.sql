DROP TABLE IF EXISTS Recent_Observations;

CREATE TABLE Recent_Observations (
	Index SERIAL PRIMARY KEY,
	Species_Code VARCHAR(10),
    Common_Name VARCHAR(30),
    Scientific_Name VARCHAR(50),
    Location_ID INTEGER,
    Location_Name VARCHAR(50),
    Observation_Date DATE,
    Quantity_Observed INTEGER,
    Latitude VARCHAR(15),
    Longitude VARCHAR(15),
    Location_Private BOOLEAN
);