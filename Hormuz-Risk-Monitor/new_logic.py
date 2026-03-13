import math
def calculate_hormuz_gamma(price, days):
    return 1.0 + (0.15 * math.log(days + 1) * (price / 100))
