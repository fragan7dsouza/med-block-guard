import requests

API_URL = "http://127.0.0.1:8000/verify"

trial_id = "NCT06382246" 

correct_data = "{'nct_id': 'NCT06382246', 'title': 'The Acute Effect of 2 Exercise Snacks...', 'status': 'COMPLETED'}"
tampered_data = "{'nct_id': 'NCT06382246', 'title': 'The Acute Effect of 3 Exercise Snacks...', 'status': 'COMPLETED'}"

def check_integrity(nct_id, data_to_check, label):
    response = requests.get(f"{API_URL}/{nct_id}", params={"current_data": data_to_check})
    result = response.json()
    print(f"--- {label} ---")
    print(f"integrity valid: {result['integrity_valid']}")
    print(f"hash: {result['current_hash']}\n")

if __name__ == "__main__":
    check_integrity(trial_id, correct_data, "checking original data")
    check_integrity(trial_id, tampered_data, "checking tampered data")