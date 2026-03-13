#!/bin/bash

# 1. Capture the session data
echo "--- Bloomberg Session Entry: $(date +'%Y-%m-%d') ---"
read -p "Enter Brent Close Price: " brent
read -p "Enter Nasdaq Close Index: " nasdaq
read -p "Enter Days Above Pivot ($100): " days

# 2. Update the C++ source file using sed
# We look for the variable assignment and replace the value
sed -i "s/double brent_close = .*;/double brent_close = $brent;/g" RiskMonitor.cpp
sed -i "s/double nasdaq_close = .*;/double nasdaq_close = $nasdaq;/g" RiskMonitor.cpp
sed -i "s/int consecutive_days = .*;/int consecutive_days = $days;/g" RiskMonitor.cpp

echo "Logic updated. Compiling..."

# 3. Compile and Run
g++ -O3 RiskMonitor.cpp -o risk_engine

if [ $? -eq 0 ]; then
    echo "Execution successful:"
    ./risk_engine
else
    echo "Compilation failed. Check your C++ syntax."
fi
