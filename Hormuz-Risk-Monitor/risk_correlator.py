import random
from datetime import datetime

def get_risk_assessment(oil_price, tech_index):
    # Higher oil generally pressures tech margins due to energy/logistics costs
    risk_score = (oil_price / 100) * 0.7 + (tech_index / 7000) * 0.3
    
    if oil_price > 105:
        status = "🔴 CRITICAL: HORMUZ ESCALATION"
    elif oil_price > 95:
        status = "🟡 WARNING: MARGIN COMPRESSION"
    else:
        status = "🟢 STABLE: LOW ENERGY FRICTION"
        
    return round(risk_score, 2), status

# March 12, 2026 Spot Data
oil_spot = 102.45  # WTI Crude
nasdaq_pivot = 22105.36

score, msg = get_risk_assessment(oil_spot, nasdaq_pivot)

print(f"\n{'='*50}")
print(f"🌍 HORMUZ RISK MONITOR | {datetime.now().strftime('%Y-%m-%d')}")
print(f"{'='*50}")
print(f"WTI Crude Spot: ${oil_spot}")
print(f"Tech Sentiment: {msg}")
print(f"Systemic Risk Score: {score}/1.0")
print(f"{'='*50}")

if score > 0.8:
    print("ACTION: Execute 10% Hedge into Treasury Bonds (WELSUS66)")
else:
    print("ACTION: Maintain 70/20/10 Position")
