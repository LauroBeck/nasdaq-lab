import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Bloomberg-style Dark Mode
plt.style.use('dark_background')

def generate_intelligence_chart():
    print("🚀 Extracting Macro Data (Nasdaq vs. Brent Crude)...")
    
    # 2026 Market Tickers
    nasdaq_ticker = "^IXIC"
    brent_ticker = "BZ=F" # Brent Crude Futures
    
    # Fetch 1 month of data for trend analysis
    nasdaq_data = yf.download(nasdaq_ticker, period="1mo", interval="1d")
    brent_data = yf.download(brent_ticker, period="1mo", interval="1d")

    fig, ax1 = plt.subplots(figsize=(14, 8), dpi=100)

    # --- Primary Axis: Nasdaq ---
    color_nasdaq = '#00d4ff' # Electric Blue
    ax1.set_ylabel('NASDAQ COMPOSITE', color=color_nasdaq, fontweight='bold', fontsize=12)
    ax1.plot(nasdaq_data.index, nasdaq_data['Close'], color=color_nasdaq, linewidth=3, label='Nasdaq Index')
    ax1.tick_params(axis='y', labelcolor=color_nasdaq)
    ax1.fill_between(nasdaq_data.index, nasdaq_data['Close'].min(), nasdaq_data['Close'], color=color_nasdaq, alpha=0.05)
    ax1.grid(color='#333333', linestyle='--', alpha=0.5)

    # --- Secondary Axis: Brent Crude ---
    ax2 = ax1.twinx()
    color_oil = '#ff9900' # Deep Orange
    ax2.set_ylabel('BRENT CRUDE ($/BBL)', color=color_oil, fontweight='bold', fontsize=12)
    ax2.plot(brent_data.index, brent_data['Close'], color=color_oil, linewidth=2.5, linestyle='--', label='Brent Crude')
    ax2.tick_params(axis='y', labelcolor=color_oil)

    # Horizontal Line for the $80 Breakout
    ax2.axhline(y=80, color='red', linestyle=':', linewidth=1.5, alpha=0.8)
    ax2.annotate('CRITICAL $80 BREAKOUT', xy=(nasdaq_data.index[-5], 80.5), color='red', fontweight='bold')

    # Titles and Meta
    plt.title(f'INTELLIGENCE REPORT: ENERGY SURGE VS. TECH EQUITY\nStatus: {datetime.now().strftime("%Y-%m-%d %H:%M")} | Market Pressure: HIGH', 
              loc='left', fontsize=14, pad=20)
    
    fig.tight_layout()
    
    # Save the output
    output_path = 'research/energy_impact_2026.png'
    plt.savefig(output_path)
    print(f"📈 Chart successfully archived to: {output_path}")

if __name__ == "__main__":
    generate_intelligence_chart()
