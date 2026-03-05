import nasdaqdatalink
import os
import pandas as pd

# 1. Setup
api_key = os.getenv("NASDAQ_API_KEY")
nasdaqdatalink.ApiConfig.api_key = api_key

# Select essential columns
selected_columns = ['ticker', 'per_end_date', 'tot_revnu', 'eps_basic_net']

print("🚀 Fetching latest 10 rows for MSFT and AAPL...")

try:
    # 2. Fetch WITHOUT the date filter to confirm connectivity
    # We use qopts={'rows': 10} to just get a sample quickly
    data = nasdaqdatalink.get_table(
        'ZACKS/FC', 
        ticker=['MSFT', 'AAPL'], 
        qopts={'columns': selected_columns, 'rows': 10},
        paginate=True
    )

    if data.empty:
        print("❌ Still Empty. Let's try fetching just one ticker without any filters...")
        data = nasdaqdatalink.get_table('ZACKS/FC', ticker='MSFT', qopts={'rows': 5})

    if not data.empty:
        # Convert date and sort
        data['per_end_date'] = pd.to_datetime(data['per_end_date'])
        data = data.sort_values(by='per_end_date', ascending=False)
        
        print("\n--- Latest Financials ---")
        print(data)
    else:
        print("❌ No data found. Your API key might not have a subscription to ZACKS/FC.")
        print("Try a free dataset like 'QUOTEMEDIA/PRICES' instead.")

except Exception as e:
    print(f"⚠️ Error: {e}")
