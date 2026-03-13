#!/bin/bash
# 1. Cleanup and Launch
fuser -k 8000/tcp 2>/dev/null
python3 bny_test_project/src/mock_gateway.py &
sleep 2

# 2. Unified Audit, Risk, and Whale Overlay
python3 << 'PYTHON'
import requests
from datetime import datetime

# CONFIG
BASE_URL = "http://localhost:8000/open-banking/v3.1/aisp"
BANKS = ["JPM", "BNY", "WFB"]
OIL_PRICE = 102.45
WHALE_DATA = {
    "NVDA": {"own": 71.2, "sig": "🟢 BUY_DIP"},
    "PLTR": {"own": 62.5, "sig": "🟢 ACCUMULATE"},
    "LMT":  {"own": 75.8, "sig": "🛡️ STRONG_HOLD"},
    "TSLA": {"own": 46.2, "sig": "🛡️ VOLATILE"}
}

print(f"\n{'='*65}")
print(f"🏛️  PRO-TERMINAL: AUDIT | RISK | WHALE SENTIMENT")
print(f"{'='*65}")

# Part A: Treasury Audit
total = 0
for b_id in BANKS:
    try:
        acc = requests.get(f"{BASE_URL}/accounts", headers={'x-fapi-financial-id': b_id}).json()['Data']['Account'][0]
        bal = float(requests.get(f"{BASE_URL}/accounts/{acc['AccountId']}/balances").json()['Data']['Balance'][0]['Amount']['Amount'])
        total += bal
        print(f"{b_id:<5} | {acc['Servicer']['Identification']:<10} | ${bal:>15,.2f}")
    except: pass
print(f"{'-'*65}")
print(f"CONSOLIDATED LIQUIDITY: ${total:>40,.2f}")

# Part B: Risk & Whale Overlay
risk = round((OIL_PRICE / 100) * 0.7 + (6845 / 7000) * 0.3, 2)
print(f"\nHORMUZ RISK: {risk}/1.0 | {'🔴 RED ALERT' if risk > 0.8 else '🟢 STABLE'}")
print(f"{'-'*65}")
print(f"{'WHALE WATCH (BIG 7 Banks)':<30} | {'OWNERSHIP':<10} | {'SIGNAL'}")
for t, d in WHALE_DATA.items():
    print(f"{t:<30} | {d['own']:>9}% | {d['sig']}")

print(f"{'='*65}\n")
PYTHON
