import nasdaqdatalink
import os
import pandas as pd

# 1. Setup
api_key = os.getenv("NASDAQ_API_KEY")
nasdaqdatalink.ApiConfig.api_key = api_key

# 2. Define the metrics we actually care about (to avoid 249 columns)
# Note: 'per_end_date' is the standard column for the filing period end.
selected_columns = [
    'ticker', 
    'per_end_date', 
    'tot_revnu', 
    'net_income_loss_share_holder', 
    'eps_basic_net'
]

print("🚀 Fetching refined data for MSFT and AAPL...")

try:
    # 3. Request with filters
    # gte = "Greater Than or Equal to"
    data = nasdaqdatalink.get_table(
        'ZACKS/FC', 
        ticker=['MSFT', 'AAPL'], 
        per_end_date={'gte': '2023-01-01'},
        qopts={'columns': selected_columns},
        paginate=True
    )

    # 4. Sort by date for better readability
    data['per_end_date'] = pd.to_datetime(data['per_end_date'])
    data = data.sort_values(by=['ticker', 'per_end_date'], ascending=[True, False])

    print("\n--- Refined Financials (Millions) ---")
    print(data)

    # 5. Save locally
    data.to_csv("tech_fundamentals.csv", index=False)
    print("\n✅ Saved to tech_fundamentals.csv")

except Exception as e:
    print(f"❌ Error: {e}")
