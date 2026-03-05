import yfinance as yf
import pandas as pd

# In 2026, the ticker for the Nasdaq Composite is ^IXIC
print("🚀 Fetching live 2026 Nasdaq Composite data...")

try:
    # Get the last 5 days of data
    nasdaq = yf.Ticker("^IXIC")
    df = nasdaq.history(period="5d")

    if not df.empty:
        print("\n--- Nasdaq Composite (^IXIC) - Actual 2026 Levels ---")
        # Formatting for readability
        print(df[['Open', 'High', 'Low', 'Close', 'Volume']].tail())
        
        current_price = df['Close'].iloc[-1]
        print(f"\n✅ Current Market Level: {current_price:.2f}")
    else:
        print("❌ No data returned. Check your internet connection.")

except Exception as e:
    print(f"⚠️ Error: {e}")
