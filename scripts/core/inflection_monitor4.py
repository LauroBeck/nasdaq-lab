import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d
from datetime import datetime

# --- UI Config ---
plt.style.use('dark_background')
BOLD, RED, GREEN, RESET = '\033[1m', '\033[91m', '\033[92m', '\033[0m'

def find_inflection_points(data, sigma=2):
    """Detects where trend acceleration changes sign (Second Derivative)"""
    # Smooth data to remove 2026 'noise' from geopolitical spikes
    smoothed = gaussian_filter1d(data, sigma=sigma)
    # Second derivative: Rate of change of the rate of change
    d2 = np.gradient(np.gradient(smoothed))
    # Inflection occurs where d2 crosses zero
    inflections = np.where(np.diff(np.sign(d2)))[0]
    return smoothed, d2, inflections

def run_inflection_lab():
    print(f"📡 {BOLD}CORE ANALYSIS: NASDAQ VS S&P 500 INFLECTION ENGINE{RESET}")
    
    # 1. Pull 2026 Data
    tickers = ["^IXIC", "^GSPC"] # Nasdaq & S&P 500
    df = yf.download(tickers, period="3mo", interval="1d", multi_level_index=False)['Close']
    
    nas_raw = df['^IXIC'].dropna()
    spx_raw = df['^GSPC'].dropna()

    # 2. Calculate Mathematical Inflections
    nas_smooth, nas_d2, nas_infl = find_inflection_points(nas_raw)
    spx_smooth, spx_d2, spx_infl = find_inflection_points(spx_raw)

    # 3. Detect Divergence (The 'Real' Signal)
    # Is Nasdaq accelerating down while S&P is accelerating up?
    nas_accel = nas_d2[-1]
    spx_accel = spx_d2[-1]
    
    print(f"{'-'*60}")
    print(f"Nasdaq Accel: {nas_accel:+.4f} | S&P 500 Accel: {spx_accel:+.4f}")
    
    if np.sign(nas_accel) != np.sign(spx_accel):
        print(f"{RED}{BOLD}🚨 CRITICAL DIVERGENCE DETECTED{RESET}")
        print("Market is splitting: Tech and Broad Market are accelerating in opposite directions.")
    else:
        print(f"{GREEN}✅ MOMENTUM SYNCED{RESET}: Both indices share acceleration signs.")
    print(f"{'-'*60}")

    # 4. High-Fidelity Visualization
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    
    # Chart 1: Price & Inflection Points
    ax1.plot(nas_raw.index, nas_raw, color='#00d4ff', alpha=0.3, label='Nasdaq Raw')
    ax1.plot(nas_raw.index, nas_smooth, color='#00d4ff', linewidth=2, label='Nasdaq Trend')
    ax1.scatter(nas_raw.index[nas_infl], nas_smooth[nas_infl], color='white', s=50, zorder=5, label='Inflection Pt')
    ax1.set_title("PRICE ACTION & MATHEMATICAL TURNING POINTS", loc='left')
    ax1.legend()

    # Chart 2: Acceleration (The Leading Indicator)
    ax2.plot(nas_raw.index, nas_d2, color='#ff9900', label='Nasdaq Acceleration (d2)')
    ax2.axhline(0, color='white', linestyle='--', alpha=0.5)
    ax2.fill_between(nas_raw.index, 0, nas_d2, where=(nas_d2 > 0), color='green', alpha=0.2)
    ax2.fill_between(nas_raw.index, 0, nas_d2, where=(nas_d2 < 0), color='red', alpha=0.2)
    ax2.set_ylabel("ACCELERATION")
    
    plt.tight_layout()
    plt.savefig('research/true_inflection.png')
    print(f"📈 Real-time Inflection Map generated: {BOLD}research/true_inflection.png{RESET}")

if __name__ == "__main__":
    run_inflection_lab()
