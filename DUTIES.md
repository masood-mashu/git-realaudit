# Separation of Duties for GitRealAudit

In accordance with compliance standards and zero-trust engineering principles, all critical operations require dual-party authorization.

## Role Definitions

### Maker
The RealEstateAcquisitionsAnalyst who builds underwriting pro formas and models property cash flows.

### Checker
The InvestmentCommitteeDirector who evaluates risk metrics, verifies loan covenants, and approves capital deployment.

## Enforcement Mechanism
No configuration, manifest, or policy change evaluated by GitRealAudit may be merged without explicit validation by the independent Checker. The system enforces cryptographic integrity across both roles.
