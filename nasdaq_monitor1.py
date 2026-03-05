import yfinance as yf
import os
import time

def send_notification(title, message):
    """Sends a native Linux desktop notification with session awareness."""
    # We find your User ID (usually 1000) to point to the correct DBUS path
    user_id = os.getuid()
    
    # This command tells Linux: "I'm the logged-in user, show this on my screen"
    cmd = (
        f'DISPLAY=:0 XDG_RUNTIME_DIR=/run/user/{user_id} '
        f'notify-send "{title}" "{message}"'
    )
    os.system(cmd)

def monitor_nasdaq():
    print("🕵️ Nasdaq Monitor Active... Press Ctrl+C to stop.")
    ticker = yf.Ticker("^IXIC")
    
    while True:
        try:
            # period="2d" ensures we have enough data to calculate change
            df = ticker.history(period="2d")
            
            if len(df) < 2:
                time.sleep(10)
                continue

            prev_close = df['Close'].iloc[-2]
            current_price = df['Close'].iloc[-1]
            change_pct = ((current_price - prev_close) / prev_close) * 100

            # Alert if market moves significantly (e.g., > 0.1% for testing)
            if abs(change_pct) >= 0.1: 
                direction = "📈 UP" if change_pct > 0 else "📉 DOWN"
                msg = f"Nasdaq {direction} {change_pct:.2f}% | Price: {current_price:.2f}"
                send_notification("Nasdaq Lab Alert", msg)
                print(f"🔔 Alert Sent: {msg}")

            time.sleep(60) # Check every minute

        except Exception as e:
            print(f"⚠️ Connection error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    monitor_nasdaq()
