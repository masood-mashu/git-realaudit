"""
dscr_covenant_auditor.py - Audits Debt Service Coverage Ratio where DSCR is Net Operating Income divided by Annual Debt Service
"""
import sys
import json


def audit_dscr(noi_dollars: float, annual_debt_service: float, min_covenant: float = 1.25):
    dscr = round(noi_dollars / annual_debt_service, 2) if annual_debt_service > 0 else 0.0
    passes_covenant = dscr >= min_covenant
    return {"dscr": dscr, "minimum_required": min_covenant, "compliant": passes_covenant, "status": "COVENANT_MET" if passes_covenant else "COVENANT_BREACH"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "dscr-covenant-auditor"}))
