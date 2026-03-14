import sys
def analyze_fox_data(sp500_val, nasdaq_val, brent_val):
    print(f"--- Fox Market Intelligence Snapshot ---")
    print(f"S&P 500: {sp500_val} | Nasdaq: {nasdaq_val} | Brent: ${brent_val}")
    tech_drag, energy_lead = -0.93, 2.67
    spread = energy_lead - tech_drag
    print(f"Current Tech-to-Energy Spread: {spread:.2f}%")
    if spread > 3.0: print("SIGNAL: Significant Sector Rotation Detected.")

if __name__ == "__main__":
    analyze_fox_data(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
