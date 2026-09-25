"""
lease_escalation_verifier.py - Calculates compounded future annual lease payment based on annual percentage increase
"""
import sys
import json


def calculate_lease_escalation(base_rent: float, annual_increase_pct: float, years: int):
    future_rent = round(base_rent * ((1 + (annual_increase_pct / 100)) ** years), 2)
    return {"base_rent": base_rent, "annual_increase_pct": annual_increase_pct, "years": years, "future_rent": future_rent, "status": "CALCULATED"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "lease-escalation-verifier"}))
