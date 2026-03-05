import os
import sys
from datetime import datetime

# --- Dependency Check ---
try:
    import yfinance as yf
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.ndimage import gaussian_filter1d
except ImportError:
    print("❌ Run: /root/nasdaq_project/venv/bin/pip install scipy yfinance matplotlib numpy")
    sys.exit(1)

# Bloomberg-style Terminal UI
plt.style.use('dark_background')
BOLD, RED, GREEN, CYAN, RESET = '\033[1m', '\033[91m', '\033[92m', '\033[96m', '\033[0m'

def run_advanced_inflection():
    print(f"\n{BOLD}🏛️  NASDAQ LAB: 2026 MACRO INFLECTION ENGINE{RESET}")
    print(f"{'='*70}")

    # 1. 2026 Data Feed: Benchmarks & Macro Drivers
    # ^IXIC (Nasdaq), ^GSPC (S&P 500), BZ=F (Brent Crude), ^TNX (10Y Yield)
    tickers = ["^IXIC", "^GSPC", "BZ=F", "^TNX"]
    data = yf.download(tickers, period="3mo", interval="1d", multi_level_index=False)['Close']
    
    nas_raw = data['^IXIC'].dropna()
    spx_raw = data['^GSPC'].dropna()
    brent_px = data['BZ=F'].iloc[-1]
    yield_10y = data['^TNX'].iloc[-1]

    # 2. Gaussian Inflection Logic (Sigma 2 for 2026 Geopolitical Noise)
    def get_accel(series):
        smooth = gaussian_filter1d(series, sigma=2)
        return smooth, np.gradient(np.gradient(smooth))

    nas_smooth, nas_d2 = get_accel(nas_raw)
    spx_smooth, spx_d2 = get_accel(spx_raw)
    
    # Inflection Points (Acceleration Sign Change)
    nas_infl = np.where(np.diff(np.sign(nas_d2)))[0]

    # 3. Market Regime Detection
    # Brent Crude at $84.75 is the 2026 "Inflation Trigger"
    energy_risk = "HIGH" if brent_px > 80 else "STABLE"
    
    # Divergence Check: Is tech decelerating while broad market accelerates?
    divergence = np.sign(nas_d2[-1]) != np.sign(spx_d2[-1])
    divergence_signal = f"{RED}🚨 ACTIVE DIVERGENCE{RESET}" if divergence else f"{GREEN}✅ SYNCED{RESET}"

    # 4. Terminal Intelligence Report
    print(f"{BOLD}DATE:{RESET}   {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{BOLD}ENERGY:{RESET} Brent Crude at {RED}${brent_px:.2f}{RESET} (Risk: {energy_risk})")
    print(f"{BOLD}BONDS:{RESET}  10Y Yield at {CYAN}{yield_10y:.2f}%{RESET}")
    print(f"{BOLD}SIGNAL:{RESET} {divergence_signal}")
    print(f"{'-'*70}")

    # 5. Visualization Engine
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True, gridspec_kw={'height_ratios': [2, 1]})

    # Top Plot: Trend & Turning Points
    ax1.plot(nas_raw.index, nas_raw, color='#00d4ff', alpha=0.3, label='Nasdaq Raw')
    ax1.plot(nas_raw.index, nas_smooth, color='#00d4ff', linewidth=2.5, label='Nasdaq Trend')
    ax1.scatter(nas_raw.index[nas_infl], nas_smooth[nas_infl], color='white', s=70, zorder=5, label='Inflection Pt')
    
    # Mark the 100-DMA Breach on SPX
    ax1.set_title("STRATEGIC INFLECTION: MOMENTUM DECOUPLING", loc='left', fontsize=14)
    ax1.legend(loc='upper left')

    # Bottom Plot: Acceleration (The Leading Signal)
    ax2.plot(nas_raw.index, nas_d2, color='#ff9900', linewidth=2, label='Nasdaq Acceleration (d2)')
    ax2.axhline(0, color='white', linestyle='--', alpha=0.5)
    ax2.fill_between(nas_raw.index, 0, nas_d2, where=(nas_d2 > 0), color='green', alpha=0.2)
    ax2.fill_between(nas_raw.index, 0, nas_d2, where=(nas_d2 < 0), color='red', alpha=0.2)
    ax2.set_ylabel("ACCEL (TREND CHANGE)")
    
    plt.tight_layout()
    plt.savefig('research/true_inflection.png')
    print(f"📈 Strategic Map Saved: {BOLD}research/true_inflection.png{RESET}\n")

if __name__ == "__main__":
    run_advanced_inflection()
