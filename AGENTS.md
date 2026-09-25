# Multi-Agent Workflow Orchestration

GitRealAudit coordinates evaluation, safety verification, and compliance approval across specialized agent personas.

## Pipeline Architecture
1. **Step 1**: Ingest historical property operating statements and tenant rent rolls.
2. **Step 2**: Calculate Net Operating Income (NOI) by subtracting operating expenses from effective gross income.
3. **Step 3**: Compute Capitalization Rate against acquisition purchase price.
4. **Step 4**: Audit debt covenants including DSCR and loan-to-value (LTV) constraints.

## Separation of Agents

Maker: RealEstateAcquisitionsAnalyst who builds underwriting pro formas and models property cash flows.

Checker: InvestmentCommitteeDirector who evaluates risk metrics, verifies loan covenants, and approves capital deployment.
