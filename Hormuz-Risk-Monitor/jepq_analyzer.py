import numpy as np

def jepq_performance_audit(nav_price, ndx_close, ndx_delta, jepq_delta):
    # Calculate the 'Yield Support Level'
    # High NDX volatility increases JEPQ's premiums even if the price dips slightly
    vol_cushion = abs(ndx_delta) - abs(jepq_delta)
    
    print(f"\n--- JEPQ Dashboard Audit | 2026-03-13 ---")
    print(f"Current NAV: ${nav_price}")
    print(f"NDX Resistance: {vol_cushion:+.4f}% Alpha over Nasdaq")
    
    # Logic based on the chart spike at 10:00 AM
    if vol_cushion > 0.8:
        print("RESULT: High Volatility Capture. JEPQ is effectively shorting the fear.")
    else:
        print("RESULT: Low Volatility Capture. Monitor for premium decay.")

if __name__ == "__main__":
    # Data from image: JEPQ $56.52, NDX 22105.36, NDX -0.93%, JEPQ -0.07%
    jepq_performance_audit(56.52, 22105.36, -0.93, -0.07)
