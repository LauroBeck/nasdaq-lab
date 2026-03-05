import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage import gaussian_filter1d
from datetime import datetime

# --- Bloomberg Terminal UI ---
plt.style.use('dark_background')
BOLD, RED, GREEN, CYAN, RESET = '\033[1m', '\033[91m', '\033[92m', '\033[96m', '\033[0m'

def run_ibm_intelligence():
    print(f"\n{BOLD}🏛️  IBM STRATEGIC RECOVERY MONITOR | MARCH 05, 2026{RESET}")
    print(f"{'='*70}")

    # 1. Fetch 2026 Real-Time Data
    # IBM, Nasdaq (^IXIC), and the 10Y Yield (^TNX)
    tickers = ["IBM", "^IXIC", "^TNX"]
    data = yf.download(tickers, period="1mo", interval="1d", multi_level_index=False)['Close']
    
    ibm = data['IBM'].dropna()
    nasdaq = data['^IXIC'].dropna()
    yield_10y = data['^TNX'].iloc[-1]

    # 2. Inflection Logic: Second Derivative (Acceleration)
    # We use Sigma 1.5 for stock-specific smoothing
    def get_mom(series):
        smooth = gaussian_filter1d(series, sigma=1.5)
        accel = np.gradient(np.gradient(smooth))
        return smooth, accel

    ibm_smooth, ibm_accel = get_mom(ibm)
    nas_smooth, nas_accel = get_mom(nasdaq)

    # 3. Intelligence Metrics
    current_ibm = ibm.iloc[-1]
    ibm_daily_change = ((current_ibm - ibm.iloc[-2]) / ibm.iloc[-2]) * 100
    
    # Inflection Signal: Is IBM accelerating while the Nasdaq stalls?
    recovery_signal = "STRONG RECOVERY" if ibm_accel[-1] > 0 and nas_accel[-1] < 0 else "MARKET SYNC"
    
    # 4. Terminal Report
    print(f"IBM PRICE:   {GREEN}${current_ibm:.2f}{RESET} ({ibm_daily_change:+.2f}%)")
    print(f"BOND YIELD:  {CYAN}{yield_10y:.2f}%{RESET} (High yield favors Value/IBM)")
    print(f"MOMENTUM:    {BOLD}{recovery_signal}{RESET}")
    print(f"{'-'*70}")

    # 5. Visualization
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True, gridspec_kw={'height_ratios': [2, 1]})

    # Top Plot: IBM vs Nasdaq Normalized
    ibm_norm = (ibm / ibm.iloc[0]) * 100
    nas_norm = (nasdaq / nasdaq.iloc[0]) * 100
    
    ax1.plot(ibm.index, ibm_norm, color='#0062ff', linewidth=3, label='IBM (Normalized)')
    ax1.plot(nasdaq.index, nas_norm, color='#ffffff', linewidth=1.5, label='NASDAQ (Benchmark)', alpha=0.5)
    ax1.set_title("IBM RELATIVE STRENGTH & RECOVERY INFLECTION", loc='left', fontsize=14)
    ax1.legend()

    # Bottom Plot: IBM Acceleration
    ax2.plot(ibm.index, ibm_accel, color='#ff9900', label='IBM Acceleration (d2)')
    ax2.axhline(0, color='white', linestyle='--', alpha=0.3)
    ax2.fill_between(ibm.index, 0, ibm_accel, where=(ibm_accel > 0), color='green', alpha=0.2)
    ax2.fill_between(ibm.index, 0, ibm_accel, where=(ibm_accel < 0), color='red', alpha=0.2)
    ax2.set_ylabel("RECOVERY FORCE")

    plt.tight_layout()
    plt.savefig('research/ibm_inflection.png')
    print(f"📈 Strategic Map Saved: {BOLD}research/ibm_inflection.png{RESET}\n")

if __name__ == "__main__":
    run_ibm_intelligence()
