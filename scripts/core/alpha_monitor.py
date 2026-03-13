# 🏛️ Financial Intelligence Suite 2026
# Session Date: March 11, 2026 (Oracle Earnings Day)

def run_alpha_sweep():
    # Final Close Data (Verified Mar 11, 2026)
    nasdaq_pct = 0.08
    
    portfolio = {
        "ORCL": {"price": 163.12, "delta": 9.18, "tag": "AI Cloud Surge"},
        "TSLA": {"price": 407.82, "delta": 2.15, "tag": "Robotics Momentum"},
        "IBM":  {"price": 248.87, "delta": -0.53, "tag": "Post-Div Pullback"},
        "JPM":  {"price": 287.52, "delta": -0.42, "tag": "Macro Yield Drag"}
    }
    
    print(f"📊 ALPHA REPORT | MAR 11, 2026 | IXIC Baseline: {nasdaq_pct}%")
    print("-" * 65)
    print(f"{'Ticker':<6} | {'Price':<8} | {'Alpha vs IXIC':<15} | {'Note'}")
    print("-" * 65)
    
    for ticker, m in portfolio.items():
        alpha = m['delta'] - nasdaq_pct
        status = "🟢" if alpha > 0 else "🔴"
        print(f"{ticker:<6} | ${m['price']:>7.2f} | {status} {alpha:>+6.2f}% | {m['tag']}")

if __name__ == "__main__":
    run_alpha_sweep()
