import random
import matplotlib.pyplot as plt


def simulation(n):
    heads = 0
    tails = 0
    for i in range(n):
        if random.choice([0, 1]) == 0:
            heads += 1
        else:
            tails += 1
    return heads, tails


def run_tests():
    for n in [1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8, 1e9, 1e10]:
        n = int(n)
        heads, tails = simulation(n)

        fig = plt.figure(figsize=(10, 5))

        # creating the bar plot
        plt.bar(["Heads", "Tails"], [heads, tails], color='red', width=0.4)

        plt.xlabel("Type")
        plt.ylabel("Count")
        plt.title(f"Heads vs. Tails in {n} trials.")
        plt.show()
        print(f"TRIAL WITH {n} TERMS: heads-{heads}, tails-{tails}")


def analysis():
    x = [52, 50.4, 49.5, 49.9, 49.9, 50, 50, 50, 50]
    y = [48, 49.6, 50.5, 50.1, 50.1, 50, 50, 50, 50]
    n = [2, 3, 4, 5, 6, 7, 8, 9, 10]

    plt.plot(n, x, label="Heads")
    plt.plot(n, y, label="Tails")
    plt.title("Percentage Heads and Tails over log(n)")
    plt.xlabel("log(n)")
    plt.ylabel("Percentages")
    plt.legend()
    plt.show()


analysis()
