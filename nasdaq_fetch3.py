import nasdaqdatalink
import os
import pandas as pd

# 1. Setup
api_key = os.getenv("NASDAQ_API_KEY")
nasdaqdatalink.ApiConfig.api_key = api_key

# Essential columns for a clean view
selected_columns = ['ticker', 'per_end_date', 'tot_revnu', 'eps_basic_net']

print("🚀 Fetching data for MSFT and AAPL...")

try:
    # 2. Corrected Fetch
    # - Removed 'rows' (it's not supported in get_table)
    # - Using 'paginate=True' is the standard for tables
    data = nasdaqdatalink.get_table(
        'ZACKS/FC', 
        ticker=['MSFT', 'AAPL'], 
        qopts={'columns': selected_columns},
        paginate=True
    )

    if not data.empty:
        # 3. Clean and Sort
        data['per_end_date'] = pd.to_datetime(data['per_end_date'])
        
        # Get the most recent 10 records after fetching
        data = data.sort_values(by='per_end_date', ascending=False).head(10)
        
        print("\n--- Latest Financials (Success) ---")
        print(data)
    else:
        print("❌ The query returned no data. Check if your API key has ZACKS/FC access.")

except Exception as e:
    # This will catch if the API key is invalid or permissions are missing
    print(f"⚠️ API Error: {e}")
