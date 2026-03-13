# ==========================================
# GLOBAL MACRO MARKET ENGINE
# Author: Lauro Beck
# Project: Financial Intel 2026
# ==========================================

import pandas as pd
import yfinance as yf


# ==========================================
# MARKET DATA ENGINE
# ==========================================

class MarketDataEngine:

    def fetch_prices(self):

        tickers = {
            "SP500": "^GSPC",
            "NASDAQ100": "^NDX",
            "BRENT": "BZ=F",
            "GOLD": "GC=F",
            "USD": "DX-Y.NYB"
        }

        results = {}

        for name, ticker in tickers.items():

            try:

                data = yf.download(
                    ticker,
                    period="2d",
                    interval="1d",
                    progress=False
                )

                close_today = float(data["Close"].iloc[-1])
                close_yesterday = float(data["Close"].iloc[-2])

                change = ((close_today - close_yesterday) / close_yesterday) * 100

                results[name] = round(change, 2)

            except Exception as e:

                print(f"Data error for {name}: {e}")
                results[name] = 0.0

        return results


# ==========================================
# MACRO PROPAGATION MODEL
# ==========================================

class MacroPropagationModel:

    def __init__(self):

        self.beta = {

            "NasdaqMomentum": 1.25,
            "DefenseSector": 0.75,
            "EnergySector": 0.55,
            "GoldReaction": -0.35,
            "USDReaction": -0.25

        }

    def propagate(self, sp_move):

        predictions = {}

        for asset, sensitivity in self.beta.items():

            move = sp_move * sensitivity
            predictions[asset] = round(move, 2)

        return predictions


# ==========================================
# WAR / OIL SHOCK ADJUSTMENT
# ==========================================

class OilShockAdjustment:

    def adjust(self, predictions, oil_move):

        oil_move = float(oil_move)

        print("\nOil Move Detected:", oil_move, "%")

        if oil_move > 5:

            print("⚠ OIL SHOCK DETECTED")

            predictions["EnergySector"] += round(oil_move * 0.4, 2)
            predictions["DefenseSector"] += round(oil_move * 0.3, 2)

        return predictions


# ==========================================
# MAIN ENGINE
# ==========================================

def main():

    print("\n=================================")
    print("GLOBAL MACRO MARKET ENGINE")
    print("=================================\n")

    # Fetch market data
    data_engine = MarketDataEngine()
    market = data_engine.fetch_prices()

    df = pd.DataFrame.from_dict(market, orient="index", columns=["Move%"])

    print("MARKET SNAPSHOT\n")
    print(df)
    print("\n")

    sp_move = float(market["SP500"])
    oil_move = float(market["BRENT"])

    # Run propagation model
    macro_model = MacroPropagationModel()
    predictions = macro_model.propagate(sp_move)

    # Apply oil shock adjustment
    oil_adjust = OilShockAdjustment()
    predictions = oil_adjust.adjust(predictions, oil_move)

    print("\nMACRO PROPAGATION FORECAST\n")

    for asset, move in predictions.items():

        print(asset, "->", move, "%")

    print("\n=================================\n")


# ==========================================
# PROGRAM START
# ==========================================

if __name__ == "__main__":
    main()
