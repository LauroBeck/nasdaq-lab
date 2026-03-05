import yfinance as yf
import os
import time
import subprocess

def get_dbus_address():
    """Automatically finds the DBUS address for the current logged-in user."""
    try:
        # Try the most common modern path first
        uid = os.getuid()
        path = f"/run/user/{uid}/bus"
        if os.path.exists(path):
            return f"unix:path={path}"
        return None
    except:
        return None

def send_notification(title, message):
    """Sends a native Linux notification using the found DBUS address."""
    dbus_addr = get_dbus_address()
    
    # We build a command that explicitly points to your display
    env = os.environ.copy()
    env["DISPLAY"] = ":0"
    if dbus_addr:
        env["DBUS_SESSION_BUS_ADDRESS"] = dbus_addr

    try:
        subprocess.run(["notify-send", title, message], env=env)
    except Exception as e:
        print(f"❌ Could not send notification: {e}")

def monitor_nasdaq():
    print("🕵️ Nasdaq Monitor Active (v2)... Press Ctrl+C to stop.")
    ticker = yf.Ticker("^IXIC")
    
    while True:
        try:
            # We fetch 2 days of data to calculate the move from 'Yesterday's Close'
            df = ticker.history(period="2d")
            
            if len(df) < 2:
                time.sleep(10)
                continue

            prev_close = df['Close'].iloc[-2]
            current_price = df['Close'].iloc[-1]
            change_pct = ((current_price - prev_close) / prev_close) * 100

            # ALERT LOGIC: Trigger on ANY move > 0.1% for this test
            if abs(change_pct) >= 0.1: 
                direction = "📈 UP" if change_pct > 0 else "📉 DOWN"
                msg = f"Nasdaq {direction} {change_pct:.2f}% | Price: {current_price:.2f}"
                
                print(f"🔔 Alert Triggered: {msg}")
                send_notification("Nasdaq Lab Alert", msg)

            # Wait 60 seconds before checking again
            time.sleep(60)

        except Exception as e:
            print(f"⚠️ Connection error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    monitor_nasdaq()
