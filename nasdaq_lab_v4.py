import yfinance as yf
import time
import os
from datetime import datetime

# Formatting
GREEN, RED, BOLD, RESET = '\033[92m', '\033[91m', '\033[1m', '\033[0m'

# Add the tickers you want to watch here
WATCHLIST = ["^IXIC", "AAPL", "MSFT", "TSLA", "NVDA"]

def get_ticker_data(symbol):
    ticker = yf.Ticker(symbol)
    df = ticker.history(period="2d")
    if len(df) < 2: return None
    
    cur = df['Close'].iloc[-1]
    prev = df['Close'].iloc[-2]
    chg_pct = ((cur - prev) / prev) * 100
    return {"price": cur, "pct": chg_pct}

def build_dashboard():
    os.system('clear')
    print(f"{BOLD}🖥️  NASDAQ LAB PORTFOLIO MONITOR | {datetime.now().strftime('%Y-%m-%d')}{RESET}")
    print(f"{'TICKER':<10} {'PRICE':<12} {'CHANGE %':<10}")
    print("-" * 35)

    for sym in WATCHLIST:
        data = get_ticker_data(sym)
        if data:
            color = GREEN if data['pct'] >= 0 else RED
            # Clean up the name for the index
            display_name = "NASDAQ" if sym == "^IXIC" else sym
            print(f"{display_name:<10} {data['price']:<12,.2f} {color}{data['pct']:+8.2f}%{RESET}")
    
    print("-" * 35)
    print(f"Last Sync: {datetime.now().strftime('%H:%M:%S')} | Press Ctrl+C to Exit")

if __name__ == "__main__":
    try:
        while True:
            build_dashboard()
            time.sleep(15) # Refresh every 15 seconds
    except KeyboardInterrupt:
        print("\n🛑 Monitor Closed.")
