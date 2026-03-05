import yfinance as yf
import time
import os
from datetime import datetime

# ANSI Color Codes for the terminal
GREEN = '\033[92m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'

def log_alert(message):
    """Saves the alert to a local log file."""
    with open("nasdaq_alerts.log", "a") as f:
        f.write(f"{datetime.now()}: {message}\n")

def run_dashboard():
    os.system('clear')
    print(f"{BOLD}🚀 Nasdaq Real-Time Dashboard (2026){RESET}")
    print("------------------------------------------")
    ticker = yf.Ticker("^IXIC")
    
    while True:
        try:
            # Fetch data
            df = ticker.history(period="2d")
            if len(df) < 2:
                continue

            prev_close = df['Close'].iloc[-2]
            current_price = df['Close'].iloc[-1]
            change = current_price - prev_close
            change_pct = (change / prev_close) * 100

            # Determine color
            color = GREEN if change >= 0 else RED
            symbol = "▲" if change >= 0 else "▼"

            # Update the Terminal (Overwrites the same line)
            timestamp = datetime.now().strftime("%H:%M:%S")
            output = (
                f"\r{BOLD}[{timestamp}]{RESET} Nasdaq: "
                f"{color}{current_price:,.2f} {symbol} {change_pct:+.2f}%{RESET} "
                f"(Vol: {df['Volume'].iloc[-1]:,})"
            )
            print(output, end="", flush=True)

            # Log significant moves (> 0.5%) to file
            if abs(change_pct) >= 0.5:
                log_alert(f"ALERT: Nasdaq {change_pct:.2f}% at {current_price:.2f}")

            time.sleep(10) # Update every 10 seconds

        except KeyboardInterrupt:
            print(f"\n\n{BOLD}🛑 Dashboard Stopped.{RESET}")
            break
        except Exception as e:
            print(f"\n⚠️ Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    run_dashboard()
