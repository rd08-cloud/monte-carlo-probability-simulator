
# Monte Carlo Probability Simulator

## Overview
A Python-based project that uses Monte Carlo simulation to estimate the probability of obtaining at least two sixes when rolling five fair dice.

## Mathematical Concept
The project demonstrates:
- Random experiments
- Probability estimation
- Theoretical vs experimental probability
- Absolute error
- Law of Large Numbers
- Probability convergence

## Theoretical Probability

Let X represent the number of sixes obtained when rolling five dice.

The probability of obtaining at least two sixes is:

P(X >= 2) = 1 - P(X = 0) - P(X = 1)

The theoretical probability is approximately 19.6245%.

## Technologies Used
- Python
- NumPy
- Matplotlib

## How to Run

1. Download this repository.
2. Install the dependencies:

   python -m pip install -r requirements.txt

3. Run the program:

   python main.py

4. Enter the number of simulation trials.

## Visualisation

The convergence graph compares the simulated probability with the theoretical probability as the number of experiments increases.

![Convergence Graph](screenshots/probability_convergence.png) 

## Learning Outcomes
This project helped me explore and evaluate probability theory, random simulations, statistical estimation, Python programming and data visualisation.
