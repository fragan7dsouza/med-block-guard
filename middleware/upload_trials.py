import pandas as pd
import requests

CSV_PATH = "../data/trials_with_bias_scores.csv"
API_URL = "http://127.0.0.1:8000/register-trial"

def upload_data():
    df = pd.read_csv(CSV_PATH)
    
    for index, row in df.iterrows():
        params = {
    "nct_id": row['nct_id'],
    "title": row['title'],
    "trial_data": str({
        "nct_id": row['nct_id'],
        "title": row['title'],
        "gender": row['gender'],
        "min_age": row['min_age'],
        "bias_risk": row['bias_risk_level']
    })
}
        
        response = requests.post(API_URL, params=params)
        
        if response.status_code == 200:
            print(f"successfully registered: {row['nct_id']}")
        else:
            print(f"failed to register {row['nct_id']}: {response.text}")

if __name__ == "__main__":
    upload_data()