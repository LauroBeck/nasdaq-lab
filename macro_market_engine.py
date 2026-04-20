import pandas as pd
import numpy as np

class MarketEngine:
    def __init__(self):
        # HARD-SYNC: Bloomberg Terminal Data @ 2026-04-20 Close
        self.telemetry = {
            "SPX": {
                "val": 7109.14, 
                "change": -0.24, 
                "pivot": 7000.00, 
                "recovery_target": 6500.00
            },
            "NDX": {
                "val": 24404.39, 
                "change": -0.26, 
                "resistance": 24500.00
            },
            "BRENT": {
                "val": 96.30, 
                "risk_threshold": 90.00, 
                "intraday_spike": 4.32
            },
            "IBM": {
                "val": 253.71, 
                "sentiment": "BULLISH_SAFE_HAVEN", 
                "earnings_date": "2026-04-22"
            },
            "ORCL": {
                "val": 176.90, 
                "sentiment": "OVERSOLD_RECOVERY"
            }
        }

    def calculate_rebound_alpha(self):
        """
        Calculates probability of SP500 positive rebound.
        Weighting: (Distance from 7k Support) vs (Oil Drag Penalty)
        """
        spx_val = self.telemetry["SPX"]["val"]
        spx_pivot = self.telemetry["SPX"]["pivot"]
        brent_val = self.telemetry["BRENT"]["val"]
        brent_limit = self.telemetry["BRENT"]["risk_threshold"]

        # Alpha Logic: Every dollar Brent is above $90 adds 1.25 penalty points
        oil_drag = max(0, brent_val - brent_limit) * 1.25
        support_strength = (spx_val - spx_pivot) / 10
        
        alpha_score = support_strength - oil_drag
        return round(alpha_score, 2)

    def generate_terminal_report(self):
        alpha = self.calculate_rebound_alpha()
        brent_val = self.telemetry["BRENT"]["val"]
        
        print(f"\n{'='*45}")
        print(f" SYSTEM STATUS: NASDAQ REACTIVE ENV - 2026-04-20")
        print(f"{'='*45}")
        print(f" SPX CURRENT: {self.telemetry['SPX']['val']} ({self.telemetry['SPX']['change']}%)")
        print(f" BRENT CRUDE: ${brent_val} (+{self.telemetry['BRENT']['intraday_spike']}%)")
        print(f" REBOUND ALPHA: {alpha}")
        print(f"{'-'*45}")

        # Logic-Based Alerts
        if brent_val > 95:
            print(f"[CRITICAL] HORMUZ RISK: Oil at ${brent_val} blocking tech expansion.")
        
        if self.telemetry["SPX"]["val"] > self.telemetry["SPX"]["pivot"]:
            print(f"[STATUS] POSITIVE: SPX holding above 7,000 baseline.")

        if alpha > 0:
            print(f"[SIGNAL] STRATEGY: MAINTAIN BULLISH PIVOT. REBOUND ACTIVE.")
        else:
            print(f"[SIGNAL] STRATEGY: HEDGE SECTORS. MONITOR 6,500 FLOOR.")
        
        print(f"{'='*45}\n")

if __name__ == "__main__":
    engine = MarketEngine()
    engine.generate_terminal_report()
