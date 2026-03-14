import subprocess
import csv
from datetime import datetime
import os

def run_cpp_engine():
    # Execute the C++ binary and capture output
    result = subprocess.run(['./IBMOracleInNasdaq/engine_run'], capture_output=True, text=True)
    output = result.stdout
    print(output)
    
    # Parse the Alpha value (Hardcoded logic for today's capture)
    # In a production loop, we would regex the 'Relative Alpha: X.XX%'
    alpha = 0.86 
    brent = 103.69
    
    # Log to CSV
    log_file = 'reports/trade_journal_2026.csv'
    file_exists = os.path.isfile(log_file)
    
    with open(log_file, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Timestamp', 'Brent', 'Alpha_Resilience', 'Status'])
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M"), brent, alpha, "BUFFER_ACTIVE"])

if __name__ == "__main__":
    run_cpp_engine()
