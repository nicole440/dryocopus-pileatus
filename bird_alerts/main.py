from datetime import date
import pandas as pd
from send_emails import send_emails
import os
from dotenv import load_dotenv
load_dotenv()

# SHEET_NAME = "Sheet1"
# SHEET_ID = os.getenv("SHEET_ID")
# url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

# def load_df(url):
#     df = pd.read_csv(url, parse_dates = ['date'])
#     return df

# Parse CSV file containing email alert data and load into DataFrame
data = f"email_data.csv"
def load_df(data):
    df = pd.read_csv(data, parse_dates = ['date'])
    return df

def query_data_and_send_emails(df):
    present = date.today()
    email_counter = 0
    for _, row in df.iterrows():
        if (present == row["date"].date() and row["rare_bird"] == True):
            send_emails(
                subject=f'Bird Alert! {row["species"]}',
                name=row["name"],
                recipient_email=row["email"],
                species=row["species"],
                rare_bird=row["rare_bird"],
                date=row["date"].strftime("%B %d, %Y"),
                location_name=row["location_name"]
            )
        email_counter += 1
    return f"Total Emails Sent: {email_counter}"

df = load_df(data)
result = query_data_and_send_emails(df)
print(df)
print(result)