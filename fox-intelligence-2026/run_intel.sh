#!/bin/bash
# FOX-INTELLIGENCE-2026: Main Execution Chain
echo "--- Initializing Fox Intel Suite (March 13 Session) ---"

# 1. Activate Virtual Environment
source venv/bin/activate || { echo "Error: venv not found"; exit 1; }

# 2. Run Python JP Logic with latest data
# Inputs: Brent(103.69) Nasdaq_Delta(-0.93) JEPQ_Delta(-0.07)
python3 jp_logic.py 103.69 -0.93 -0.07

# 3. Synchronize Workspace to GitHub
git add .
git commit -m "DATA: Restore session March 13 - Brent Pivot 103.69"
git push origin main

echo "--- Logic Executed and Pushed to Fox-Intelligence-2026 ---"
