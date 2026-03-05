import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Bloomberg Intelligence Theme
plt.style.use('dark_background')

def analyze_inflection():
    print("📡 Monitoring Nasdaq vs. S&P 500 Inflection Point (2026)...")
    
    # 1. Fetching Core Benchmarks (Fixing the 2026 Multi-Index structure)
    nasdaq_df = yf.download("^IXIC", period="1mo", interval="1d", multi_level_index=False)
    sp500_df = yf.download("^GSPC", period="1mo", interval="1d", multi_level_index=False)
    
    # Squeeze to 1D Series
    nasdaq = nasdaq_df['Close'].squeeze()
    sp500 = sp500_df['Close'].squeeze()
    
    # 2. Normalization Logic (Fixing the KeyError: 0)
    # We use .iloc[0] to get the first numeric value safely
    nasdaq_norm = (nasdaq / nasdaq.iloc[0]) * 100
    sp500_norm = (sp500 / sp500.iloc[0]) * 100
    
    # 3. Ratio Analysis (Tech Strength vs. Broad Market)
    ratio = nasdaq / sp500

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True, gridspec_kw={'height_ratios': [2, 1]})

    # --- Top Plot: Normalized Performance ---
    ax1.plot(nasdaq_norm.index, nasdaq_norm, color='#00d4ff', linewidth=2.5, label='NASDAQ (Tech)')
    ax1.plot(sp500_norm.index, sp500_norm, color='#ffffff', linewidth=1.5, label='S&P 500 (Broad)', alpha=0.8)
    
    # Highlight the Spread
    ax1.fill_between(nasdaq_norm.index, sp500_norm, nasdaq_norm, 
                     where=(nasdaq_norm >= sp500_norm), color='green', alpha=0.1, label='Tech Outperforming')
    ax1.fill_between(nasdaq_norm.index, sp500_norm, nasdaq_norm, 
                     where=(nasdaq_norm < sp500_norm), color='red', alpha=0.1, label='Tech Underperforming')

    ax1.set_title(f'MARKET INFLECTION: TECH VS. BROAD EQUITY | {datetime.now().strftime("%Y-%m-%d")}', loc='left', fontsize=14)
    ax1.legend(loc='upper left')
    ax1.grid(color='#333333', linestyle='--', alpha=0.5)

    # --- Bottom Plot: IXIC/SPX Relative Strength ---
    ax2.plot(ratio.index, ratio, color='#ff9900', linewidth=2, label='IXIC/SPX Ratio')
    ax2.axhline(y=ratio.mean(), color='white', linestyle=':', alpha=0.5, label='Mean Ratio')
    ax2.set_ylabel('REL. STRENGTH')
    ax2.fill_between(ratio.index, ratio.min(), ratio, color='#ff9900', alpha=0.05)
    ax2.legend(loc='upper left')
    
    plt.tight_layout()
    
    output_file = 'research/nasdaq_sp500_inflection.png'
    plt.savefig(output_file)
    print(f"📈 Strategic analysis archived to: {output_file}")

if __name__ == "__main__":
    analyze_inflection()
