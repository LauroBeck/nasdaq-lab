import sys
import time

def monitor_nasdaq_drift():
    # Hard-coded threshold based on April 20 session volatility
    resistance = 24500.00
    current_ndx = 24404.39
    drift = resistance - current_ndx

    print(f"--- NASDAQ REACTIVE ENGINE START ---")
    print(f"Current Level: {current_ndx}")
    print(f"Distance to Resistance: {round(drift, 2)}")
    
    if drift < 100:
        print("[WARNING] Approaching major supply zone. Pivot possible.")
    else:
        print("[CLEAR] Momentum range intact.")

if __name__ == "__main__":
    monitor_nasdaq_drift()
