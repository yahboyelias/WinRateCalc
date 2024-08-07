
**Stock Market Prediction Game**

This Python project simulates a simplified stock market, allowing users to practice predicting daily price changes.

**Features**

* **Realistic Stock Simulation:** Generates a random series of stock prices over 30 days, starting at $100 with daily fluctuations.
* **Interactive Predictions:** Prompts the user each day to predict whether the stock price will go up, down, or stay the same.
* **Visual Feedback:** Displays a line graph of the stock prices up to the current day, aiding decision-making.
* **Performance Tracking:** Calculates and reports the user's overall win/loss ratio, providing insight into their predictive accuracy.
* **Educational:** Helps users develop an intuitive understanding of stock market trends and volatility.

**Getting Started**

1. **Prerequisites:**
   * Ensure you have Python installed on your system.
   * Install the required libraries:
     ```bash
     pip install matplotlib
     ```
2. **Running the Game:**
    * Save the provided code as a Python file (e.g., `stock_game.py`).
    * Run the file from your terminal:
     ```bash
     python stock_game.py
     ```

**Usage**

1. Observe the stock price chart for the days leading up to the current day.
2. Enter your prediction for the next day's price change:
   * `U`: Up
   * `D`: Down
   * `S`: Stay the same
3. See whether your prediction was correct or incorrect.
4. Repeat for all 30 days of the simulated stock market.
5. Review your overall win/loss ratio to gauge your performance.


**Example Interaction**

```
Day 1: Do you think the price will go up (U), down (D), or stay the same (S)? U
Incorrect prediction.

Day 2: Do you think the price will go up (U), down (D), or stay the same (S)? D
Correct prediction!

# ... Continues for 30 days ...
```

The point of this code is to find your win rate to then use with a monte carlo simulation that works best with your win %.

**License**

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

