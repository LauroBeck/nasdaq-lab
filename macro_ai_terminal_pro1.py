import cv2
import pytesseract
import pandas as pd
import re
import sys
import os

print("\n=================================")
print("GLOBAL MACRO AI TERMINAL PRO")
print("=================================\n")


# -----------------------------
# SCREEN READER
# -----------------------------

class ScreenReader:

    def read(self, path):

        if not os.path.exists(path):
            print("❌ File not found:", path)
            sys.exit()

        img = cv2.imread(path)

        if img is None:
            print("❌ Could not read image")
            sys.exit()

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # improve OCR
        gray = cv2.resize(gray, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
        gray = cv2.GaussianBlur(gray, (5,5), 0)

        text = pytesseract.image_to_string(gray)

        return text


# -----------------------------
# BLOOMBERG TEXT PARSER
# -----------------------------

class BloombergParser:

    def parse(self, text):

        data = {}

        text = text.upper()

        # BRENT PRICE
        brent = re.search(r'BRENT[^0-9]*(\d+\.\d+)', text)

        if brent:
            data["BRENT_PRICE"] = float(brent.group(1))


        # NY CRUDE
        crude = re.search(r'CRUDE[^0-9]*(\d+\.\d+)', text)

        if crude:
            data["CRUDE_PRICE"] = float(crude.group(1))


        # OIL MOVE
        oil_moves = re.findall(r'\+(\d+\.\d+)', text)

        if oil_moves:

            oil_moves = [float(x) for x in oil_moves]

            data["OIL_MOVE"] = max(oil_moves)


        # S&P FUTURES
        sp = re.search(r'S&P[^%]*(-?\d+\.\d+)%', text)

        if sp:
            data["SP500_FUT"] = float(sp.group(1))


        # NASDAQ FUTURES
        ndx = re.search(r'NDX[^%]*(-?\d+\.\d+)%', text)

        if ndx:
            data["NASDAQ_FUT"] = float(ndx.group(1))


        # DAX FUTURES
        dax = re.search(r'DAX[^%]*(-?\d+\.\d+)%', text)

        if dax:
            data["DAX_FUT"] = float(dax.group(1))


        # DOW FUTURES
        dow = re.search(r'DOW[^%]*(-?\d+\.\d+)%', text)

        if dow:
            data["DOW_FUT"] = float(dow.group(1))


        # WAR / GEOPOLITICS
        data["WAR"] = ("WAR" in text) or ("IRAN" in text)

        return data


# -----------------------------
# MACRO ENGINE
# -----------------------------

class MacroEngine:

    def compute(self, data):

        oil = data.get("OIL_MOVE",0)
        sp = data.get("SP500_FUT",0)
        nasdaq = data.get("NASDAQ_FUT",0)
        war = data.get("WAR",False)

        regime = "NEUTRAL"

        if oil > 10 and war:
            regime = "GEOPOLITICAL OIL SHOCK"

        elif sp < -1:
            regime = "RISK OFF"

        elif sp > 1:
            regime = "RISK ON"


        energy = oil * 0.4
        defense = oil * 0.25 + (1 if war else 0)
        tech = nasdaq * 1.1
        gold = oil * 0.15
        volatility = abs(sp) * 2

        forecast = {

            "EnergySector": round(energy,2),
            "DefenseSector": round(defense,2),
            "TechSector": round(tech,2),
            "GoldReaction": round(gold,2),
            "VolatilitySpike": round(volatility,2)

        }

        return regime, forecast


# -----------------------------
# TERMINAL DISPLAY
# -----------------------------

class Terminal:

    def show(self, market, regime, forecast):

        print("MARKET DATA\n")

        if market:
            print(pd.DataFrame.from_dict(market, orient="index", columns=["Value"]))
        else:
            print("⚠ No values detected")

        print("\nMACRO REGIME\n")

        print(">>>", regime)

        print("\nSECTOR FORECAST\n")

        for k,v in forecast.items():

            print(k,"->",v,"%")



# -----------------------------
# MAIN
# -----------------------------

def main():

    if len(sys.argv) < 2:

        print("Usage:")
        print("python macro_ai_terminal_pro.py bloomberg.png")
        return


    image = sys.argv[1]

    reader = ScreenReader()

    text = reader.read(image)

    # DEBUG OPTION
    # print(text)

    parser = BloombergParser()

    market = parser.parse(text)

    engine = MacroEngine()

    regime, forecast = engine.compute(market)

    terminal = Terminal()

    terminal.show(market, regime, forecast)


if __name__ == "__main__":
    main()

print("\n=================================\n")
