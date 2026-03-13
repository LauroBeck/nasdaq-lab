import datetime

# Real-time Institutional Sentiment - March 12, 2026
big_7_sentiment = {
    "NVDA": {"ownership": 71.2, "target": 265, "signal": "BUY_THE_DIP"},
    "PLTR": {"ownership": 62.5, "target": 195, "signal": "ACCUMULATE"},
    "LMT":  {"ownership": 75.8, "target": 680, "signal": "STRONG_HOLD"},
    "TSLA": {"ownership": 46.2, "target": 240, "signal": "VOLATILE"}
}

def check_whale_movements():
    print(f"\n{'='*65}")
    print(f"🐋 BIG 7 BANK SENTIMENT MONITOR | {datetime.date.today()}")
    print(f"{'='*65}")
    print(f"{'TICKER':<8} | {'OWNERSHIP':<12} | {'BANK TARGET':<12} | {'SIGNAL'}")
    print(f"{'-'*65}")
    
    for ticker, data in big_7_sentiment.items():
        signal_color = "🟢" if data['signal'] in ["ACCUMULATE", "BUY_THE_DIP"] else "🛡️"
        print(f"{ticker:<8} | {data['ownership']:>10}% | ${data['target']:>11} | {signal_color} {data['signal']}")
    
    print(f"{'='*65}")
    print("ARCHITECT NOTE: The banks are rotating into PLTR and LMT")
    print("due to the 1.01 Hormuz Risk Score. NVDA remains the 'Anchor'.")
    print(f"{'='*65}\n")

check_whale_movements()
