import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime

# Bloomberg-style Dark Mode
plt.style.use('dark_background')

def generate_intelligence_chart():
    print("🚀 Extracting Macro Data (Nasdaq vs. Brent Crude)...")
    
    # 1. Fetch data (multi_level_index=False is a 2025+ fix)
    nasdaq_df = yf.download("^IXIC", period="1mo", interval="1d", multi_level_index=False)
    brent_df = yf.download("BZ=F", period="1mo", interval="1d", multi_level_index=False)

    # 2. Squeeze the data into 1D Series to avoid the ValueError
    # We use .iloc[:, 0] to ensure we only get a 1D vector of numbers
    nasdaq_close = nasdaq_df['Close'].squeeze()
    brent_close = brent_df['Close'].squeeze()

    fig, ax1 = plt.subplots(figsize=(14, 8), dpi=100)

    # --- Primary Axis: Nasdaq ---
    color_nasdaq = '#00d4ff' 
    ax1.set_ylabel('NASDAQ COMPOSITE', color=color_nasdaq, fontweight='bold', fontsize=12)
    ax1.plot(nasdaq_df.index, nasdaq_close, color=color_nasdaq, linewidth=3, label='Nasdaq Index')
    ax1.tick_params(axis='y', labelcolor=color_nasdaq)
    
    # FIX: fill_between now receives 1D data
    ax1.fill_between(nasdaq_df.index, nasdaq_close.min(), nasdaq_close, color=color_nasdaq, alpha=0.05)
    ax1.grid(color='#333333', linestyle='--', alpha=0.5)

    # --- Secondary Axis: Brent Crude ---
    ax2 = ax1.twinx()
    color_oil = '#ff9900' 
    ax2.set_ylabel('BRENT CRUDE ($/BBL)', color=color_oil, fontweight='bold', fontsize=12)
    ax2.plot(brent_df.index, brent_close, color=color_oil, linewidth=2.5, linestyle='--', label='Brent Crude')
    ax2.tick_params(axis='y', labelcolor=color_oil)

    # Annotate the $80 Breakout
    ax2.axhline(y=80, color='red', linestyle=':', linewidth=1.5, alpha=0.8)

    plt.title(f'INTELLIGENCE REPORT: ENERGY SURGE VS. TECH EQUITY\nStatus: {datetime.now().strftime("%Y-%m-%d %H:%M")}', 
              loc='left', fontsize=14, pad=20)
    
    fig.tight_layout()
    plt.savefig('research/energy_impact_2026.png')
    print("📈 Chart successfully fixed and archived.")

if __name__ == "__main__":
    generate_intelligence_chart()
