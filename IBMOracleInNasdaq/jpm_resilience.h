#include <iostream>

void evaluate_jepq_buffer() {
    double ndx_drop = -0.93;
    double jepq_drop = -0.07;
    double alpha = jepq_drop - ndx_drop;

    std::cout << "--- JPM Resilience Report ---" << std::endl;
    std::cout << "Relative Alpha: " << alpha << "%" << std::endl;
    if (alpha > 0.5) std::cout << "STATUS: JEPQ is effectively shielding tech volatility." << std::endl;
}
