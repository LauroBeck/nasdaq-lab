import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Bloomberg Intelligence Theme
plt.style.use('dark_background')
RED, GREEN, BOLD, RESET = '\033[91m', '\033[92m', '\033[1m', '\033[0m'

def analyze_inflection():
    print(f"📡 {BOLD}CORE INTELLIGENCE: NASDAQ vs S&P 500{RESET}")
    
    # 1. Fetching Data
    nasdaq_df = yf.download("^IXIC", period="1mo", interval="1d", multi_level_index=False)
    sp500_df = yf.download("^GSPC", period="1mo", interval="1d", multi_level_index=False)
    
    nasdaq = nasdaq_df['Close'].squeeze()
    sp500 = sp500_df['Close'].squeeze()
    
    # 2. Performance Calculations
    # 1-Week (5 Trading Days) Delta
    nas_wk_chg = ((nasdaq.iloc[-1] - nasdaq.iloc[-5]) / nasdaq.iloc[-5]) * 100
    spx_wk_chg = ((sp500.iloc[-1] - sp500.iloc[-5]) / sp500.iloc[-5]) * 100
    perf_gap = nas_wk_chg - spx_wk_chg

    # 3. Terminal Alert System
    print("-" * 50)
    print(f"NASDAQ 5D: {nas_wk_chg:+.2f}% | S&P 500 5D: {spx_wk_chg:+.2f}%")
    
    if perf_gap <= -2.0:
        print(f"{RED}{BOLD}⚠️ ALERT: TECH INFLECTION POINT DETECTED{RESET}")
        print(f"Status: Nasdaq underperforming S&P 500 by {abs(perf_gap):.2f}% this week.")
        print("Action: Monitor 10Y Yields and Energy ($84+ Brent) for tech de-rating.")
    else:
        print(f"{GREEN}STATUS: Tech Correlation Stable.{RESET} Gap: {perf_gap:+.2f}%")
    print("-" * 50)

    # 4. Visualization
    nasdaq_norm = (nasdaq / nasdaq.iloc[0]) * 100
    sp500_norm = (sp500 / sp500.iloc[0]) * 100
    ratio = nasdaq / sp500

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True, gridspec_kw={'height_ratios': [2, 1]})
    ax1.plot(nasdaq_norm.index, nasdaq_norm, color='#00d4ff', linewidth=2, label='NASDAQ')
    ax1.plot(sp500_norm.index, sp500_norm, color='#ffffff', linewidth=1, label='S&P 500', alpha=0.6)
    ax1.set_title(f'MARKET INFLECTION ANALYSIS | {datetime.now().strftime("%Y-%m-%d")}', loc='left', fontsize=14)
    ax1.legend()
    
    ax2.plot(ratio.index, ratio, color='#ff9900', label='IXIC/SPX Ratio')
    ax2.fill_between(ratio.index, ratio.min(), ratio, color='#ff9900', alpha=0.05)
    
    plt.savefig('research/nasdaq_sp500_inflection.png')
    print("📈 Visual updated: research/nasdaq_sp500_inflection.png")

if __name__ == "__main__":
    analyze_inflection()
