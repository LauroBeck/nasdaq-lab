#include <iostream>
#include <vector>
#include <random>
#include <thread>
#include <algorithm>
#include <numeric>

// Simulation constants for March 13 session
const double NASDAQ_CLOSE = 22105.36;
const double DAILY_VOL = 0.015; // 1.5% daily volatility
const int SIMULATIONS = 1000000;
const int THREADS = std::thread::hardware_concurrency();

void run_sim(int n, double* results) {
    std::mt19937 gen(std::random_device{}());
    std::normal_distribution<double> dist(0.0, DAILY_VOL);
    for (int i = 0; i < n; ++i) {
        // Geometric Brownian Motion step
        results[i] = NASDAQ_CLOSE * std::exp(dist(gen));
    }
}

int main() {
    std::vector<double> results(SIMULATIONS);
    std::vector<std::thread> workers;
    int sim_per_thread = SIMULATIONS / THREADS;

    for (int i = 0; i < THREADS; ++i) {
        workers.emplace_back(run_sim, sim_per_thread, &results[i * sim_per_thread]);
    }

    for (auto& t : workers) t.join();

    std::sort(results.begin(), results.end());
    double var_95 = results[SIMULATIONS * 0.05];

    std::cout << "--- High-Perf Simulation: NASDAQ VaR ---" << std::endl;
    std::cout << "Parallel Threads: " << THREADS << std::endl;
    std::cout << "95% Confidence Level (VaR): " << var_95 << std::endl;
    std::cout << "Max Projected Weekend Drawdown: " << NASDAQ_CLOSE - var_95 << std::endl;

    return 0;
}
