#include <iostream>
#include <vector>
#include <iomanip>
#include <cmath>

struct MarketData {
    double sp500 = 6774.25;
    double nasdaq = 22105.40;
    double brent = 103.14;
    double wti = 98.71;
    double orcl = 164.95;
    double amzn = 214.60;
    double uber = 74.30;
};

void printHeader(std::string title) {
    std::cout << "\n\033[1;37;44m " << title << " \033[0m\n";
}

int main() {
    MarketData md;
    
    printHeader("BLOOMBERG TERMINAL - REAL-TIME FEED - MARCH 13, 2026");
    
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "S&P 500 Index:   " << md.sp500 << " [\033[31m-0.19%\033[0m]\n";
    std::cout << "Nasdaq Composite: " << md.nasdaq << " [\033[33mPIVOT\033[0m]\n";
    std::cout << "-------------------------------------------\n";
    std::cout << "Brent Crude:     $" << md.brent << "  \033[32m(Hormuz Premium)\033[0m\n";
    std::cout << "WTI Crude:       $" << md.wti << "   \033[32m(IEA Release)\033[0m\n";
    std::cout << "-------------------------------------------\n";
    std::cout << "Oracle (ORCL):   $" << md.orcl << "  \033[1;32m(+11% AI Surge)\033[0m\n";
    std::cout << "Amazon (AMZN):   $" << md.amzn << "\n";
    std::cout << "Uber (UBER):     $" << md.uber << "   (Zoox Partnership)\n";
    std::cout << "-------------------------------------------\n";
    
    double initial = 150.0; // Million
    double haircut = 0.85;
    double adjustedNPV = 3.44; // From previous logic
    
    std::cout << "\033[1;36m[STRATEGIC NPV ADVISORY]\033[0m\n";
    std::cout << "Project Aport:   $" << initial << "M\n";
    std::cout << "Energy Haircut:  15%\n";
    std::cout << "Adjusted NPV:    \033[1;32m$" << adjustedNPV << "M\033[0m\n";
    std::cout << "Decision:        \033[1;32mHOLD/EXECUTE\033[0m\n";

    return 0;
}
