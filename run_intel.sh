#!/bin/bash
# Mission Control Master Script
source venv/bin/activate
echo "Updating local telemetry from Bloomberg data..."
python3 macro_market_engine.py
python3 nasdaq_engine.py
echo "Monitoring complete. Logs updated in nasdaq_alerts.log"
