import yfinance as yf
import os
import time

def send_notification(title, message):
    """Sends a native Linux desktop notification."""
    os.system(f'notify-send "{title}" "{message}"')

def monitor_nasdaq():
    print("🕵️ Nasdaq Monitor Active... Press Ctrl+C to stop.")
    
    # Initial Baseline
    ticker = yf.Ticker("^IXIC")
    
    while True:
        try:
            # Fetch the most recent 2 days to compare previous close vs live price
            df = ticker.history(period="2d")
            
            if len(df) < 2:
                continue

            prev_close = df['Close'].iloc[-2]
            current_price = df['Close'].iloc[-1]
            change_pct = ((current_price - prev_close) / prev_close) * 100

            # Logic: Alert if market moves more than 0.5%
            if abs(change_pct) >= 0.5:
                direction = "📈 UP" if change_pct > 0 else "📉 DOWN"
                msg = f"Nasdaq is {direction} {change_pct:.2f}% at {current_price:.2f}"
                send_notification("Nasdaq Volatility Alert", msg)
                print(f"🔔 Alert Sent: {msg}")

            # Sleep for 60 seconds before checking again
            time.sleep(60)

        except Exception as e:
            print(f"⚠️ Connection error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    monitor_nasdaq()
