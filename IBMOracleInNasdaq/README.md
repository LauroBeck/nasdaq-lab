# IBMOracleInNasdaq | JPMorgan Resilience Suite

## Technical Objective
High-performance C++ engine designed to quantify the **Resilience Alpha** of Equity Premium Income strategies (specifically **JEPQ**) against **Nasdaq (NDX)** volatility during energy-driven market shocks.

## Current Regime: March 13, 2026
* **Scenario:** Hormuz Strait Persistence (Day 31).
* **Brent Benchmark:** $103.69.
* **Resilience Delta:** Calculates the spread between Tech drawdown and Income-seeking buffer.

## Logic Engine
The suite utilizes modular C++ headers (`jpm_resilience.h`) to evaluate systemic risk:
- **NDX Delta:** -0.93%
- **JEPQ Delta:** -0.07%
- **Resulting Alpha:** +0.86% (Positive buffer detected).

## Execution
Compile with:
\`\`\`bash
g++ -O3 main.cpp -o engine_run && ./engine_run
\`\`\`
