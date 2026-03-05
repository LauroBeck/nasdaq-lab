import nasdaqdatalink
import os
import pandas as pd

# 1. Setup
nasdaqdatalink.ApiConfig.api_key = os.getenv("NASDAQ_API_KEY")

# Adding 'net_income_loss_share_holder' to the columns
selected_cols = ['ticker', 'per_end_date', 'tot_revnu', 'net_income_loss_share_holder']

print("🚀 Calculating Profit Margins...")

try:
    data = nasdaqdatalink.get_table('ZACKS/FC', ticker=['MSFT', 'AAPL'], qopts={'columns': selected_cols}, paginate=True)

    if not data.empty:
        # Convert numeric columns to float just in case
        data['tot_revnu'] = data['tot_revnu'].astype(float)
        data['net_income_loss_share_holder'] = data['net_income_loss_share_holder'].astype(float)
        
        # 2. Calculate Profit Margin (%)
        data['profit_margin_%'] = (data['net_income_loss_share_holder'] / data['tot_revnu']) * 100
        
        # 3. Sort and Clean
        data['per_end_date'] = pd.to_datetime(data['per_end_date'])
        data = data.sort_values(['ticker', 'per_end_date'], ascending=[True, False])

        print("\n--- Financial Efficiency Report ---")
        # Showing just the top 5 for each
        print(data.groupby('ticker').head(3))
    else:
        print("No data found.")

except Exception as e:
    print(f"⚠️ Error: {e}")
