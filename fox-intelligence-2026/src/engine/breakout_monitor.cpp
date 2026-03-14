#include <iostream>
#include <vector>
#include <string>
#include <iomanip>

class VolatilityTracker {
public:
    std::string ticker;
    double current_price;
    double prev_close;

    VolatilityTracker(std::string t, double cp, double pc) 
        : ticker(t), current_price(cp), prev_close(pc) {}

    void analyze() {
        double delta = ((current_price - prev_close) / prev_close) * 100;
        std::cout << "--- " << ticker << " Breakout Analysis ---" << std::endl;
        std::cout << "Current: $" << current_price << " | Change: " << std::fixed << std::setprecision(2) << delta << "%" << std::endl;
        
        if (delta > 5.0) {
            std::cout << "SIGNAL: [EXTREME BREAKOUT] - High Volatility Detected." << std::endl;
        } else {
            std::cout << "SIGNAL: Standard Momentum." << std::endl;
        }
    }
};

int main() {
    // March 13 Data: SNDK opened ~$630, closed ~$661.62
    VolatilityTracker sndk("SNDK", 661.62, 618.82);
    sndk.analyze();
    return 0;
}
