import kaggle
import pandas as pd
import os

def extract() -> pd.DataFrame:
    API_URL = "maso0dahmed/football-players-data"
    DATA_PATH = "./data"

    os.makedirs(DATA_PATH, exist_ok=True)

    kaggle.api.dataset_download_files(API_URL, path=DATA_PATH, unzip=True)

    csv_file = None
    for file in os.listdir(DATA_PATH):
        if file.endswith(".csv"):
            csv_file = os.path.join(DATA_PATH, file)
            break

    if csv_file is None:
        raise FileNotFoundError("No CSV file found in the dataset.")

    df = pd.read_csv(csv_file)
    
    return df

df = extract()
print(df.head())
