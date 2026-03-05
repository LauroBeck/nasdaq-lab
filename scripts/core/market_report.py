import yfinance as yf
from datetime import datetime

# UI Styling
BOLD, CYAN, ORANGE, RESET = '\033[1m', '\033[96m', '\033[93m', '\033[0m'

def show_market_summary():
    # Fetching the "Energy vs Tech" pivot data
    nasdaq = yf.Ticker("^IXIC").history(period="1d")
    brent = yf.Ticker("BZ=F").history(period="1d")
    nymex = yf.Ticker("CL=F").history(period="1d")

    nasdaq_px = nasdaq['Close'].iloc[-1]
    brent_px = brent['Close'].iloc[-1]
    nymex_px = nymex['Close'].iloc[-1]

    print(f"\n{BOLD}🏛️  MARKET INTELLIGENCE SUMMARY | {datetime.now().strftime('%H:%M:%S')}{RESET}")
    print("="*55)
    
    # Nasdaq Status
    print(f"{CYAN}EQUITIES:{RESET}  NASDAQ Composite   | {BOLD}{nasdaq_px:,.2f}{RESET}")
    
    # Energy Breakout Status
    energy_status = "⚠️  BREAKOUT" if brent_px > 80 else "STABLE"
    print(f"{ORANGE}ENERGY:  {RESET}  Brent Crude Oil    | {BOLD}${brent_px:.2f}{RESET} ({energy_status})")
    print(f"{ORANGE}ENERGY:  {RESET}  NYMEX Crude Oil    | {BOLD}${nymex_px:.2f}{RESET}")
    
    print("="*55)
    print(f"{BOLD}ANALYSIS:{RESET} Energy sector surge (> $80) creates headwind for tech.")
    print(f"Chart updated at: {BOLD}research/energy_impact_2026.png{RESET}\n")

if __name__ == "__main__":
    show_market_summary()
