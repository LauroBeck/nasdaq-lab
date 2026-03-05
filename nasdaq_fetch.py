import nasdaqdatalink
import os
import pandas as pd

# 1. Pull the key from your ~/.bashrc setting
api_key = os.getenv("NASDAQ_API_KEY")

if not api_key:
    print("❌ Error: NASDAQ_API_KEY not found. Run 'source ~/.bashrc' and try again.")
else:
    nasdaqdatalink.ApiConfig.api_key = api_key
    
    print(f"✅ Authenticated with key ending in ...{api_key[-4:]}")

    try:
        # 2. Fetching Microsoft (MSFT) Fundamentals from Zacks
        # This is more reliable than the old WIKI dataset
        data = nasdaqdatalink.get_table('ZACKS/FC', ticker='MSFT')
        
        print("\n--- Recent MSFT Financial Data ---")
        print(data.head())
        
        # Optional: Save to CSV for analysis
        # data.to_csv("msft_data.csv")
        
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")
