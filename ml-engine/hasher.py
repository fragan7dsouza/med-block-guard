import hashlib
import pandas as pd

def generate_hash(row):
    combined_string = f"{row['nct_id']}{row['title']}"
    return hashlib.sha256(combined_string.encode()).hexdigest()

df = pd.read_csv('../data/sample_trials.csv')
df['blockchain_hash'] = df.apply(generate_hash, axis=1)

df.to_csv('../data/trials_for_blockchain.csv', index=False)
print('hashing complete. 10 trial fingerprints generated.')