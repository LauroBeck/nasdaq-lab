import cv2
import pytesseract
import pandas as pd
import re
import sys


print("\n=================================")
print("GLOBAL MACRO AI TERMINAL")
print("=================================\n")


# ----------------------------
# OCR SCREEN READER
# ----------------------------

class ScreenReader:

    def read(self, image_path):

        img = cv2.imread(image_path)

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        text = pytesseract.image_to_string(gray)

        return text


# ----------------------------
# MARKET DATA PARSER
# ----------------------------

class MarketParser:

    def parse(self, text):

        market = {}

        sp = re.search(r'S&P\s?500.*?(-?\d+\.\d+)', text)

        if sp:
            market["SP500"] = float(sp.group(1))

        nasdaq = re.search(r'NASDAQ.*?(-?\d+\.\d+)', text)

        if nasdaq:
            market["NASDAQ"] = float(nasdaq.group(1))

        vix = re.search(r'VIX.*?(-?\d+\.\d+)', text)

        if vix:
            market["VIX"] = float(vix.group(1))

        oil = re.search(r'BRENT.*?(-?\d+\.\d+)', text)

        if oil:
            market["BRENT"] = float(oil.group(1))

        return market


# ----------------------------
# F1 SENTIMENT
# ----------------------------

class F1Sentiment:

    def calculate(self):

        mercedes_win = True

        if mercedes_win:
            print("🏎 Mercedes strong race result → Tech optimism")
            return 0.35

        return 0


# ----------------------------
# MACRO MODEL
# ----------------------------

class MacroEngine:

    def run(self, market):

        sp = market.get("SP500",0)
        oil = market.get("BRENT",0)
        vix = market.get("VIX",0)

        f1 = F1Sentiment().calculate()

        if oil > 10:
            print("\n⚠ OIL SHOCK DETECTED")

        nasdaq_momentum = sp * 1.25 + f1
        energy_sector = oil * 0.35
        defense_sector = oil * 0.20
        gold_reaction = -sp * 0.30
        usd_reaction = oil * 0.02 + vix * 0.03

        results = {

            "NasdaqMomentum": round(nasdaq_momentum,2),
            "EnergySector": round(energy_sector,2),
            "DefenseSector": round(defense_sector,2),
            "GoldReaction": round(gold_reaction,2),
            "USDReaction": round(usd_reaction,2)

        }

        return results


# ----------------------------
# MAIN
# ----------------------------

def main():

    if len(sys.argv) < 2:

        print("Usage: python macro_ai_terminal.py screenshot.png")
        return


    image_path = sys.argv[1]

    reader = ScreenReader()

    text = reader.read(image_path)

    parser = MarketParser()

    market = parser.parse(text)

    print("\nMARKET DATA DETECTED\n")

    print(pd.DataFrame.from_dict(market, orient="index", columns=["Value"]))


    engine = MacroEngine()

    forecast = engine.run(market)

    print("\nMACRO FORECAST\n")

    for k,v in forecast.items():

        print(k,"->",v,"%")



if __name__ == "__main__":
    main()


print("\n=================================\n")
