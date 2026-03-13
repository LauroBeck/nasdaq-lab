#include <iostream>
#include <cmath>

int main() {
    double brent_close = 103.69; 
    double nasdaq_delta = -0.93;
    double jepq_delta = -0.07;
    
    double buffer = jepq_delta - nasdaq_delta;
    
    std::cout << "--- JP Risk Monitor: March 13 ---" << std::endl;
    std::cout << "Brent Threshold: " << (brent_close > 100 ? "BREACHED" : "STABLE") << std::endl;
    std::cout << "JPMorgan Buffer: " << buffer << "%" << std::endl;
    
    if (buffer > 0.8) {
        std::cout << "ACTION: Volatility is being paid out via JEPQ dividends. Hold." << std::endl;
    }
    return 0;
}

/**
 * JP Risk Buffer Check
 * Validates if JEPQ premiums can cover the cost of capital (10Y Yield)
 */
void checkYieldStress(double jepq_yield_est, double us10y) {
    double spread = jepq_yield_est - us10y;
    
    std::cout << "\n[ JPM Income Stress Test ]" << std::endl;
    std::cout << "Estimated JEPQ Yield: " << jepq_yield_est << "%" << std::endl;
    std::cout << "US 10Y Benchmark:     " << us10y << "%" << std::endl;
    std::cout << "Net Spread:           " << spread << "%" << std::endl;

    if (spread < 5.0) {
        std::cout << "WARNING: Yield spread narrowing. Tech income buffer is thinning." << std::endl;
    } else {
        std::cout << "STATUS: Spread healthy. JEPQ maintaining institutional attraction." << std::endl;
    }
}
