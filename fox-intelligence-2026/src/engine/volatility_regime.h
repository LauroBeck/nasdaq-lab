#ifndef VOLATILITY_REGIME_H
#define VOLATILITY_REGIME_H

/* * FOX-INTELLIGENCE-2026 
 * Monday Open Parameters: 2026-03-16 
 */

namespace MarketRisk {
    const double BRENT_PIVOT = 103.69;
    const double NASDAQ_DELTA = -0.93;
    const double JEPQ_STRESS = -0.07;
    
    // Logarithmic scaling factor for weekend gap risk
    inline double calculate_gap_risk(double stress_idx) {
        return (stress_idx > 2.0) ? 1.45 : 1.12; 
    }
}

#endif
