import os
import sys

# --- Safe Dependency Check ---
try:
    import yfinance as yf
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.ndimage import gaussian_filter1d
except ImportError as e:
    print(f"\n❌ MISSING DEPENDENCY: {e}")
    print(f"👉 Run: /root/nasdaq_project/venv/bin/pip install scipy yfinance matplotlib numpy")
    sys.exit(1)

from datetime import datetime

# UI Config
plt.style.use('dark_background')
BOLD, RED, GREEN, RESET = '\033[1m', '\033[91m', '\033[92m', '\033[0m'

def find_inflection_points(data, sigma=2):
    """Detects where trend acceleration changes sign (Second Derivative)"""
    smoothed = gaussian_filter1d(data, sigma=sigma)
    d2 = np.gradient(np.gradient(smoothed))
    inflections = np.where(np.diff(np.sign(d2)))[0]
    return smoothed, d2, inflections

def run_inflection_lab():
    print(f"\n📡 {BOLD}CORE ANALYSIS: NASDAQ VS S&P 500 INFLECTION ENGINE (MARCH 2026){RESET}")
    print(f"{'-'*70}")
    
    # 1. Pull 2026 Data (Multi-Index fix included)
    tickers = ["^IXIC", "^GSPC"] 
    df = yf.download(tickers, period="3mo", interval="1d", multi_level_index=False)['Close']
    
    nas_raw = df['^IXIC'].dropna()
    spx_raw = df['^GSPC'].dropna()

    # 2. Calculate Mathematical Inflections
    nas_smooth, nas_d2, nas_infl = find_inflection_points(nas_raw)
    spx_smooth, spx_d2, spx_infl = find_inflection_points(spx_raw)

    # 3. Detect Divergence
    nas_accel = nas_d2[-1]
    spx_accel = spx_d2[-1]
    
    # Inflection Mood Logic
    if np.sign(nas_accel) != np.sign(spx_accel):
        signal = f"{RED}🚨 CRITICAL DIVERGENCE (Tech vs Broad Market){RESET}"
    else:
        signal = f"{GREEN}✅ MOMENTUM SYNCED{RESET}"

    print(f"NASDAQ ACCEL: {nas_accel:+.4f}")
    print(f"S&P 500 ACCEL: {spx_accel:+.4f}")
    print(f"MARKET SIGNAL: {signal}")
    print(f"{'-'*70}")

    # 4. Visualization
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)
    
    ax1.plot(nas_raw.index, nas_raw, color='#00d4ff', alpha=0.3, label='Nasdaq Raw')
    ax1.plot(nas_raw.index, nas_smooth, color='#00d4ff', linewidth=2, label='Nasdaq Trend')
    ax1.scatter(nas_raw.index[nas_infl], nas_smooth[nas_infl], color='white', s=60, edgecolors='black', zorder=5, label='Inflection Pt')
    ax1.set_title(f"PRICE ACTION & INFLECTION POINTS | {datetime.now().strftime('%Y-%m-%d')}", loc='left', fontsize=14)
    ax1.legend()
    ax1.grid(alpha=0.1)

    ax2.plot(nas_raw.index, nas_d2, color='#ff9900', label='Nasdaq Acceleration (d2)')
    ax2.axhline(0, color='white', linestyle='--', alpha=0.5)
    ax2.fill_between(nas_raw.index, 0, nas_d2, where=(nas_d2 > 0), color='green', alpha=0.2)
    ax2.fill_between(nas_raw.index, 0, nas_d2, where=(nas_d2 < 0), color='red', alpha=0.2)
    ax2.set_ylabel("ACCELERATION")
    
    plt.tight_layout()
    output_file = 'research/true_inflection.png'
    plt.savefig(output_file)
    print(f"📈 Strategic analysis archived to: {BOLD}{output_file}{RESET}")

if __name__ == "__main__":
    run_inflection_lab()
