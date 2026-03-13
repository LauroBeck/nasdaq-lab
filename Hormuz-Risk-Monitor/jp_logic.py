import sys
import numpy as np

def run_jepq_check(brent, ndx_delta, jepq_delta):
    resilience = jepq_delta - ndx_delta
    print(f"\n--- JP Session Analysis: 2026-03-13 ---")
    print(f"Brent Crude: ${brent} | NDX: {ndx_delta}% | JEPQ: {jepq_delta}%")
    print(f"Resilience Alpha: {resilience:+.2f}%")
    
    if resilience > 0.8:
        print("STATUS: JEPQ income cushion is OPTIMAL (Buffering Tech Volatility)")

if __name__ == "__main__":
    run_jepq_check(float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))
