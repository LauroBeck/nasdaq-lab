import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Bloomberg Intelligence Theme
plt.style.use('dark_background')

def analyze_inflection():
    print("📡 Monitoring Nasdaq/SP500 Inflection (2026 Macro Context)...")
    
    # 1. Fetching Core Benchmarks
    nasdaq = yf.download("^IXIC", period="1mo", multi_level_index=False)['Close'].squeeze()
    sp500 = yf.download("^GSPC", period="1mo", multi_level_index=False)['Close'].squeeze()
    
    # 2. Ratio Analysis (Nasdaq Price / S&P 500 Price)
    # A falling ratio indicates Tech is weakening relative to the broad market
    ratio = nasdaq / sp500

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True, gridspec_kw={'height_ratios': [2, 1]})

    # --- Top Plot: Comparative Performance ---
    ax1.plot(nasdaq.index, (nasdaq / nasdaq[0]) * 100, color='#00d4ff', label='NASDAQ (Normalized)')
    ax1.plot(sp500.index, (sp500 / sp500[0]) * 100, color='#ffffff', label='S&P 500 (Normalized)', alpha=0.7)
    ax1.set_title(f'MARKET INFLECTION: TECH VS. BROAD EQUITY | {datetime.now().strftime("%Y-%m-%d")}', loc='left')
    ax1.legend()
    ax1.grid(alpha=0.2)

    # --- Bottom Plot: The Ratio Line ---
    ax2.plot(ratio.index, ratio, color='#ff9900', linewidth=2, label='IXIC/SPX Ratio')
    ax2.axhline(y=ratio.mean(), color='gray', linestyle='--', alpha=0.5)
    ax2.set_ylabel('REL. STRENGTH')
    ax2.fill_between(ratio.index, ratio.min(), ratio, color='#ff9900', alpha=0.1)
    
    plt.tight_layout()
    plt.savefig('research/nasdaq_sp500_inflection.png')
    print("📈 Inflection analysis archived to research/nasdaq_sp500_inflection.png")

if __name__ == "__main__":
    analyze_inflection()
