from fastapi import FastAPI
import hashlib
import json
import os

app = FastAPI()
LEDGER_FILE = "ledger.json"

def load_ledger():
    if os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, "r") as f:
            return json.load(f)
    return {}

def save_ledger(data):
    with open(LEDGER_FILE, "w") as f:
        json.dump(data, f)

mock_ledger = load_ledger()

@app.post("/register-trial")
def register_trial(nct_id: str, title: str, trial_data: str):
    trial_hash = hashlib.sha256(trial_data.encode()).hexdigest()
    mock_ledger[nct_id] = {
        "title": title,
        "hash": trial_hash,
        "status": "Verified"
    }
    save_ledger(mock_ledger)
    return {"message": "trial registered", "hash": trial_hash}

@app.get("/verify/{nct_id}")
def verify_trial(nct_id: str, current_data: str):
    if nct_id not in mock_ledger:
        return {"error": "trial not found"}
    
    stored_hash = mock_ledger[nct_id]["hash"]
    current_hash = hashlib.sha256(current_data.encode()).hexdigest()
    
    is_valid = stored_hash == current_hash
    return {"integrity_valid": is_valid, "stored_hash": stored_hash, "current_hash": current_hash}