import requests
import pandas as pd
import time
import os
from datetime import datetime

TOKEN = "INPUT_YOUR_TOKEN_HERE"
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
REPO = "pandas-dev/pandas"

def fetch_with_retry(category, target_count):
    all_data = []
    filename = f"pandas_{category}_raw.csv"
    filepath = os.path.join(os.getcwd(), "data", "raw", filename)
    
    if os.path.exists(filepath):
        try:
            existing_df = pd.read_csv(filepath)
            all_data = existing_df.to_dict('records')
            print(f"♻️ Melanjutkan data {category} yang sudah ada: {len(all_data)} item.")
        except:
            pass

    current_until = datetime.now().isoformat()
    if all_data:
        current_until = all_data[-1]['created_at']

    print(f"🚀 Mencari sisa data {category}...")

    while len(all_data) < target_count:
        endpoint = "issues" if category == "issues" else "pulls"
        url = f"https://api.github.com/repos/{REPO}/{endpoint}"
        params = {"state": "closed", "per_page": 100, "sort": "created", "direction": "desc", "until": current_until}

        try:
            response = requests.get(url, headers=HEADERS, params=params, timeout=30)
            
            if response.status_code == 200:
                data = response.json()
                if not data: break
                
                if category == "issues":
                    filtered = [item for item in data if "pull_request" not in item]
                else:
                    filtered = [item for item in data if item.get("merged_at") is not None]
                
                all_data.extend(filtered)
                print(f"   ✅ Terkumpul: {len(all_data)} / {target_count}")

                pd.DataFrame(all_data).to_csv(filepath, index=False)
                
                current_until = data[-1]['created_at']
                time.sleep(2)
            else:
                print(f"⚠️ API Error {response.status_code}. Menunggu 10 detik...")
                time.sleep(10)
                
        except Exception as e:
            print(f"📡 Koneksi drop: {e}. Mencoba lagi dalam 5 detik...")
            time.sleep(5)
            continue
            
    return all_data

os.makedirs('data/raw', exist_ok=True)
fetch_with_retry("issues", 1000)
fetch_with_retry("prs", 500)
print("\n✨ SELESAI SEMPURNA!")