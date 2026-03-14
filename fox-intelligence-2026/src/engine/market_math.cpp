#include <iostream>
#include <vector>
#include <numeric>

int main() {
    std::vector<double> intraday_points = {47100.0, 46900.0, 46750.0, 46600.0, 46558.47};
    double sum = std::accumulate(intraday_points.begin(), intraday_points.end(), 0.0);
    double mean = sum / intraday_points.size();
    std::cout << "Fox Market Engine Active" << std::endl;
    std::cout << "Mean Intraday Index Level: " << mean << std::endl;
    std::cout << "Closing Status: BEARISH TREND" << std::endl;
    return 0;
}
