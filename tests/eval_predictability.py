"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitRealAudit.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.cap_rate_calculator import *
from tools.dscr_covenant_auditor import *
from tools.lease_escalation_verifier import *
from tools.vacancy_rate_sanity_checker import *

class TestGitRealAuditPredictability(unittest.TestCase):

    def test_01_cap_rate_calculation(self):
        res = calculate_cap_rate(noi_dollars=350000.0, purchase_price=5000000.0)
        self.assertEqual(res["cap_rate_percent"], 7.0)
        self.assertEqual(res["status"], "APPROVED")

    def test_02_dscr_covenant_pass(self):
        res = audit_dscr(noi_dollars=350000.0, annual_debt_service=250000.0, min_covenant=1.25)
        self.assertTrue(res["compliant"])
        self.assertEqual(res["dscr"], 1.4)

    def test_03_lease_escalation_calculation(self):
        res = calculate_lease_escalation(base_rent=100000.0, annual_increase_pct=3.0, years=2)
        self.assertEqual(res["future_rent"], 106090.0)


if __name__ == "__main__":
    unittest.main()
