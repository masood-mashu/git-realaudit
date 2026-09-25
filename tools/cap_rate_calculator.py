"""
cap_rate_calculator.py - Calculates Capitalization Rate where Cap Rate is Net Operating Income divided by Purchase Price times 100
"""
import sys
import json


def calculate_cap_rate(noi_dollars: float, purchase_price: float):
    cap_rate = round((noi_dollars / purchase_price) * 100, 2) if purchase_price > 0 else 0.0
    is_standard = 4.0 <= cap_rate <= 12.0
    return {"noi": noi_dollars, "purchase_price": purchase_price, "cap_rate_percent": cap_rate, "standard_range": is_standard, "status": "APPROVED" if is_standard else "ABNORMAL_CAP_RATE"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "cap-rate-calculator"}))
