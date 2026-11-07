import numpy as np
from math import comb
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


# Simulating one 5-dice experiment
def run_experiment():
    dice = np.random.randint(1, 7, size=5)
    sixes = np.count_nonzero(dice == 6)
    return sixes >= 2


# Simulating multiple 5-dice experiments
def run_simulation(total_trials):
    successful_trials = 0
    probabilities = []

    for trial in range(1, total_trials + 1):
        if run_experiment():
            successful_trials += 1

        current_probability = successful_trials / trial
        probabilities.append(current_probability)

    return probabilities


def theoretical_probability():
    probability = 1 - (5 / 6) ** 5 - comb(5, 1) * (1 / 6) * (5 / 6) ** 4
    return probability


def calculate_error(theoretical, simulated):
    error = abs(theoretical - simulated)
    return error


# Code for Graph Visualization
def plot_convergence(probabilities):
    theoretical = theoretical_probability()

    plt.plot(probabilities, label="Simulated Probability")
    plt.axhline(y=theoretical, linestyle="--", label="Theoretical Probability")

    plt.xlabel("Number of Experiments")
    plt.ylabel("Estimated Probability")
    plt.title("Monte Carlo Probability Convergence")
    plt.legend()
    plt.grid(True)
    plt.savefig("screenshots/probability_convergence.png")
    plt.close()



# Main program to calculate the estimated probability
def main():

    try:
        trials = int(input("Enter the number of trials: "))

        if trials <= 0:
            print("Please enter a positive number.")
            return

    except ValueError:
        print("Please enter a valid integer.")
        return

    probabilities = run_simulation(trials)

    simulated = probabilities[-1]
    theoretical = theoretical_probability()

    error = calculate_error(theoretical, simulated)

    print("\n--- Monte Carlo Simulation Results ---")

    print("Total trials:", trials)
    print("Theoretical probability:", theoretical * 100, "%")
    print("Simulated probability:", simulated * 100, "%")
    print("Absolute error:", error * 100, "percentage points")

    plot_convergence(probabilities)


if __name__ == "__main__":
    main()




