"""
vacancy_rate_sanity_checker.py - Verifies that property pro forma assumes at least a 5% physical and economic vacancy allowance
"""
import sys
import json


def check_vacancy_allowance(assumed_vacancy_pct: float, min_allowance: float = 5.0):
    is_conservative = assumed_vacancy_pct >= min_allowance
    return {"assumed_vacancy": assumed_vacancy_pct, "min_allowance": min_allowance, "prudent_underwriting": is_conservative, "status": "PASS" if is_conservative else "AGGRESSIVE_UNDERWRITING"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "vacancy-rate-sanity-checker"}))
