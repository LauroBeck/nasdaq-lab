import cv2
import pytesseract
import pandas as pd
import re
import sys
import os


print("\n=================================")
print("GLOBAL MACRO AI TERMINAL")
print("=================================\n")


# ----------------------------
# OCR SCREEN READER
# ----------------------------

class ScreenReader:

    def read(self, image_path):

        img = cv2.imread(image_path)

        if img is None:
            raise Exception("❌ Could not load image: " + image_path)

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
            print("🏎 Mercedes result → Tech optimism")
            return 0.35

        return 0


# ----------------------------
# MACRO ENGINE
# ----------------------------

class MacroEngine:

    def run(self, market):

        sp = market.get("SP500",0)
        oil = market.get("BRENT",0)
        vix = market.get("VIX",0)

        f1 = F1Sentiment().calculate()

        if oil > 10:
            print("⚠ OIL SHOCK DETECTED")

        nasdaq = sp * 1.25 + f1
        energy = oil * 0.35
        defense = oil * 0.20
        gold = -sp * 0.30
        usd = oil * 0.02 + vix * 0.03

        return {

            "NasdaqMomentum": round(nasdaq,2),
            "EnergySector": round(energy,2),
            "DefenseSector": round(defense,2),
            "GoldReaction": round(gold,2),
            "USDReaction": round(usd,2)

        }


# ----------------------------
# MAIN
# ----------------------------

def main():

    if len(sys.argv) < 2:

        print("Usage:")
        print("python macro_ai_terminal.py screenshot.png")
        return


    image_path = sys.argv[1]

    if not os.path.exists(image_path):
        print("❌ File not found:", image_path)
        return


    reader = ScreenReader()

    text = reader.read(image_path)

    parser = MarketParser()

    market = parser.parse(text)

    if not market:
        print("⚠ No market data detected in screenshot")
        return


    print("\nMARKET DATA DETECTED\n")

    df = pd.DataFrame.from_dict(market, orient="index", columns=["Value"])

    print(df)


    engine = MacroEngine()

    forecast = engine.run(market)

    print("\nMACRO FORECAST\n")

    for k,v in forecast.items():
        print(k,"->",v,"%")



if __name__ == "__main__":
    main()

print("\n=================================\n")
