#include <iostream>
#include "jpm_resilience.h"

int main() {
    std::cout << "--- IBMOracleInNasdaq Intelligence Suite ---" << std::endl;
    std::cout << "Session Date: 2026-03-13" << std::endl;
    
    // Execute JPM JEPQ Resilience Check
    evaluate_jepq_buffer();
    
    return 0;
}
