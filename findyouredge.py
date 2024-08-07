import random
import matplotlib.pyplot as plt


def generate_stock_prices(days):
    """Generates simulated stock prices for a given number of days."""
    price = 100  # Starting price
    prices = [price]
    for _ in range(days):
        change = random.uniform(-5, 5)  # Daily price change
        price += change
        prices.append(price)
    return prices


def stock_game():
    """Runs the stock market game."""
    days = 30  # Number of days to simulate
    prices = generate_stock_prices(days)

    correct_predictions = 0
    total_predictions = 0

    for i in range(1, days):
        plt.plot(prices[:i])
        plt.xlabel("Days")
        plt.ylabel("Price")
        plt.title("Stock Price Chart")
        plt.show()

        prediction = input(f"Day {i}: Do you think the price will go up (U), down (D), or stay the same (S)? ").upper()
        total_predictions += 1

        if (prediction == "U" and prices[i] > prices[i - 1]) or \
                (prediction == "D" and prices[i] < prices[i - 1]) or \
                (prediction == "S" and prices[i] == prices[i - 1]):
            correct_predictions += 1
            print("Correct prediction!")
        else:
            print("Incorrect prediction.")

    win_loss_ratio = correct_predictions / total_predictions
    print(f"\nOverall Win/Loss Ratio: {win_loss_ratio:.2f}")


if __name__ == "__main__":
    stock_game()
