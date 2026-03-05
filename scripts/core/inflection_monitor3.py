import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import os

# --- Bloomberg-Style Terminal Formatting ---
plt.style.use('dark_background')
RED = '\033[91m'
GREEN = '\033[92m'
CYAN = '\033[96m'
BOLD = '\033[1m'
RESET = '\033[0m'

def analyze_inflection():
    print(f"\n{BOLD}📡 CORE INTELLIGENCE: NASDAQ vs S&P 500 INFLECTION{RESET}")
    print(f"{'-'*60}")

    # 1. FETCH DATA (Using 2026 Multi-Index Fix)
    # ^IXIC = Nasdaq, ^GSPC = S&P 500, BZ=F = Brent Crude, ^TNX = 10Y Treasury Yield
    tickers = ["^IXIC", "^GSPC", "BZ=F", "^TNX"]
    data = yf.download(tickers, period="1mo", interval="1d", multi_level_index=False)

    # Squeeze columns to Series
    nasdaq = data['Close']['^IXIC'].dropna()
    sp500 = data['Close']['^GSPC'].dropna()
    brent = data['Close']['BZ=F'].dropna()
    tnx = data['Close']['^TNX'].dropna()

    # 2. PERFORMANCE CALCULATIONS
    # Use .iloc[0] to avoid KeyError: 0
    nasdaq_norm = (nasdaq / nasdaq.iloc[0]) * 100
    sp500_norm = (sp500 / sp500.iloc[0]) * 100
    ratio = nasdaq / sp500

    # 5-Day Performance Delta (Rolling Inflection)
    nas_5d = ((nasdaq.iloc[-1] - nasdaq.iloc[-5]) / nasdaq.iloc[-5]) * 100
    spx_5d = ((sp500.iloc[-1] - sp500.iloc[-5]) / sp500.iloc[-5]) * 100
    perf_gap = nas_5d - spx_5d

    # 3. HIGH-DEF TERMINAL SUMMARY
    current_brent = brent.iloc[-1]
    current_yield = tnx.iloc[-1]
    
    # Conditional Mood Logic
    mood = f"{RED}⚠️  TECH EXODUS" if perf_gap <= -2.0 else f"{GREEN}✅  TECH STABLE"
    brent_status = f"{RED}${current_brent:.2f} (OVER $80){RESET}" if current_brent > 80 else f"{GREEN}${current_brent:.2f}{RESET}"
    
    print(f"{BOLD}🏛️  STRATEGIC SUMMARY | {datetime.now().strftime('%Y-%m-%d %H:%M')}{RESET}")
    print(f"ENERGY  | Brent Crude:      {brent_status}")
    print(f"BONDS   | 10Y Yield:        {CYAN}{current_yield:.2f}%{RESET}")
    print(f"RATIO   | IXIC/SPX:         {BOLD}{ratio.iloc[-1]:.4f}{RESET} (Avg: {ratio.mean():.4f})")
    print(f"SPREAD  | 5D Tech Gap:      {perf_gap:+.2f}%")
    print(f"MOOD    | Signal:           {BOLD}{mood}{RESET}")
    print(f"{'-'*60}")

    # 4. VISUALIZATION ENGINE
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True, 
                                   gridspec_kw={'height_ratios': [2, 1]})

    # Top Plot: Normalized Comp
    ax1.plot(nasdaq_norm.index, nasdaq_norm, color='#00d4ff', linewidth=2.5, label='NASDAQ (Tech)')
    ax1.plot(sp500_norm.index, sp500_norm, color='#ffffff', linewidth=1.5, label='S&P 500 (Broad)', alpha=0.7)
    ax1.fill_between(nasdaq_norm.index, sp500_norm, nasdaq_norm, 
                     where=(nasdaq_norm >= sp500_norm), color='green', alpha=0.15)
    ax1.fill_between(nasdaq_norm.index, sp500_norm, nasdaq_norm, 
                     where=(nasdaq_norm < sp500_norm), color='red', alpha=0.15)
    ax1.set_title(f"MARKET INFLECTION: RELATIVE PERFORMANCE", loc='left', fontsize=14)
    ax1.legend(loc='upper left')
    ax1.grid(color='#333333', linestyle='--', alpha=0.5)

    # Bottom Plot: The Ratio
    ax2.plot(ratio.index, ratio, color='#ff9900', linewidth=2, label='IXIC/SPX Ratio')
    ax2.axhline(y=ratio.mean(), color='white', linestyle=':', alpha=0.5)
    ax2.set_ylabel('REL. STRENGTH')
    ax2.fill_between(ratio.index, ratio.min(), ratio, color='#ff9900', alpha=0.05)
    ax2.legend(loc='upper left')

    # Save Output
    output_path = 'research/nasdaq_sp500_inflection.png'
    os.makedirs('research', exist_ok=True)
    plt.tight_layout()
    plt.savefig(output_path)
    
    print(f"📈 Strategic analysis archived to: {output_path}")

if __name__ == "__main__":
    analyze_inflection()
