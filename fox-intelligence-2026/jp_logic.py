import sys

def main():
    if len(sys.argv) < 4:
        print("Usage: python3 jp_logic.py <Brent> <NDX_Delta> <JEPQ_Delta>")
        return

    brent = float(sys.argv[1])
    ndx_delta = float(sys.argv[2])
    jepq_delta = float(sys.argv[3])

    print(f"\n--- JP Resilience Analysis ---")
    print(f"Brent Crude: ${brent} (Status: {'CRITICAL' if brent > 100 else 'STABLE'})")
    print(f"Nasdaq Delta: {ndx_delta}%")
    
    # Simple Volatility Correlation Logic
    stress_index = (abs(ndx_delta) * 1.5) + (brent / 100)
    print(f"Calculated Stress Index: {stress_index:.2f}")

if __name__ == "__main__":
    main()
